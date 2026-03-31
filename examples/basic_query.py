import os
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from sanguoagent.indexer import create_index, load_index, save_index
from sanguoagent.query_engine import get_query_engine, query_agent
from sanguoagent.settings import Settings

settings = Settings()

# 构建或加载索引
if (
    not os.path.exists(settings.VECTOR_STORE_DIR)
    or len(os.listdir(settings.VECTOR_STORE_DIR)) == 0
):
    print("正在构建索引...")
    index = create_index(settings.PROCESSED_DATA_DIR)
    save_index(index, settings.VECTOR_STORE_DIR)
    print("索引构建完成！")
else:
    print("正在加载索引...")
    index = load_index(settings.VECTOR_STORE_DIR)
    print("索引加载完成！")

# 创建查询引擎
query_engine = get_query_engine(index)

# 示例查询
questions = [
    "刘备的主要事迹有哪些？",
    "诸葛亮是如何出山的？",
    "赤壁之战的经过是什么？",
    "关羽是怎么死的？",
]
for question in questions:
    print(f"\n问: {question}")
    response = query_agent(query_engine, question)
    print(f"答: {response}")
