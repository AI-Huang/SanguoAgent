import os
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from sanguoagent.chat_engine import chat_with_agent, get_chat_engine
from sanguoagent.indexer import create_index, load_index, save_index
from sanguoagent.settings import Settings
from sanguoagent.utils import ensure_directory

settings = Settings()

# 确保目录存在
data_dir = settings.PROCESSED_DATA_DIR
vector_store_dir = settings.VECTOR_STORE_DIR
ensure_directory(data_dir)
ensure_directory(vector_store_dir)

# 构建或加载索引
if not os.path.exists(vector_store_dir) or len(os.listdir(vector_store_dir)) == 0:
    print("正在构建索引...")
    index = create_index(data_dir)
    save_index(index, vector_store_dir)
    print("索引构建完成！")
else:
    print("正在加载索引...")
    index = load_index(vector_store_dir)
    print("索引加载完成！")

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
