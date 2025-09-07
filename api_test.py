import os
api_key_value = os.getenv("GOOGLE_API_KEY")
if api_key_value is None:
    print("环境变量GOOGLE_API_KEY未设置")
else:
    print("API密钥长度:", len(api_key_value))