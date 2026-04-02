import os
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from sanguoagent.chat_engine import chat_with_agent, get_chat_engine
from sanguoagent.pipelines.load_index import load_or_create_index
from sanguoagent.settings import Settings

settings = Settings()

index = load_or_create_index()

# 创建聊天引擎
chat_engine = get_chat_engine(index)

print("三国知识聊天助手已启动！输入 'exit' 退出聊天。")

# 聊天循环
while True:
    user_input = input("你: ")
    if user_input.lower() == "exit":
        print("再见！")
        break

    response = chat_with_agent(chat_engine, user_input)
    print(f"助手: {response}")
