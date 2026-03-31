def get_query_engine(index):
    """获取查询引擎"""
    query_engine = index.as_query_engine(
        similarity_top_k=5,  # 检索前5个最相似的段落
        response_mode="compact",  # 紧凑模式，综合多个段落的信息
    )
    return query_engine


def query_agent(query_engine, question):
    """执行查询"""
    response = query_engine.query(question)
    return response
