from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
import os

def generate_script(subject,video_length,creativity,api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}为主题的视频想一个简单大气有内涵的标题")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """ 你是一位专业的创意视频的专业编剧和分镜师。根据以下标题和相关信息，为视频写一个结构完整、镜头语言丰富的视频脚本：
             1.视频标题:{title}，视频时长:{duration}分钟，生成的脚体的长度尽量遵循视频时长的要求。
             2.要求开头抓住眼球，主体部分构思新颖，叙事逻辑清晰，可运用少量视频特效增强表现，结尾需实现主题深化或情感升华。
             3.脚本需严格遵循以下格式，以markdown表格形式呈现，包含以下列：【镜号、场景、时长、画面描述、景别、运镜、台词、备注】。
             4.整体风格应与"{title}"的主题基调相吻合。
             5.脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             '''{wikipedia_search}'''""")
        ]
    )

    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(subject)

    model = ChatGoogleGenerativeAI(
        google_api_key=api_key,
        model="gemini-2.5-pro",
        temperature=creativity
    )

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject":subject}).content
    script = script_chain.invoke({"title":title,"duration":video_length,
                                  "wikipedia_search":search_result}).content

    return script, title, search_result


# print(generate_script("七夕",3,1,os.getenv("GOOGLE_API_KEY")))
