import os
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from sanguoagent.pipelines.load_index import load_or_create_index
from sanguoagent.query_engine import get_query_engine, query_agent
from sanguoagent.settings import Settings

settings = Settings()

index = load_or_create_index()

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
