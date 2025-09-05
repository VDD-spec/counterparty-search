import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ALIBABA_API_KEY')
ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
