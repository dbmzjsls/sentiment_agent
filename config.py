import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
ANALYSIS_COUNT = 2

# 导入配置文件
load_dotenv()

# LLM
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="deepseek-r1",
    temperature=0
)
