def get_chat_engine(index):
    """获取聊天引擎"""
    chat_engine = index.as_chat_engine(
        chat_mode="context",  # 基于上下文的聊天模式
        similarity_top_k=5,  # 检索前5个最相似的段落
        response_mode="compact",  # 紧凑模式，综合多个段落的信息
    )

    return chat_engine


def chat_with_agent(chat_engine, message):
    """与代理聊天"""
    response = chat_engine.chat(message)
    return response
