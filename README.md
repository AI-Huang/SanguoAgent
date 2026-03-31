# SanguoAgent

SanguoAgent 是一个基于 LlamaIndex 的三国知识问答智能代理，能够回答关于《三国演义》的各种问题。

## 功能特性

- **智能问答**：基于《三国演义》文本回答用户问题
- **上下文理解**：支持多轮对话，理解上下文语境
- **向量检索**：使用向量存储提高查询效率和准确性

## 技术栈

- **LlamaIndex**：用于构建知识索引和问答系统
- **OpenAI API**：提供语言模型能力
- **Python**：项目开发语言

## 使用

### 安装依赖

| 依赖        | 版本   |
| ----------- | ------ |
| llama_index | 0.14.19 |
| llama_index-readers-file | 0.6.0 |

```bash
pip install -r requirements.txt
```

### 数据准备

```bash
sh scripts/download_data.sh
```

### LLM API 配置

在 `.env` 文件中添加 OpenAI API 密钥

## 使用手册

### 构建索引

```bash
python examples/basic_query.py
```

### 进行问答

```bash
python examples/chat_example.py
```

## 附录：项目结构

```
SanguoAgent/
├── .env                     # 环境变量配置文件（包含 API 密钥等）
├── requirements.txt         # 项目依赖
├── README.md                # 项目说明文档
├── data/                    # 数据存储目录
│   ├── documents/           # 原始文档
│   └── vector_store/        # 向量存储目录
├── src/                     # 源代码目录
│   ├── __init__.py
│   ├── settings.py            # 配置管理
│   ├── indexer.py           # 索引创建与管理
│   ├── query_engine.py      # 查询引擎
│   ├── chat_engine.py       # 聊天引擎
│   └── utils.py             # 工具函数
├── examples/                # 示例代码
│   ├── basic_query.py       # 基本查询示例
│   └── chat_example.py      # 聊天功能示例
└── tests/                   # 测试目录
    └── test_query.py        # 查询功能测试
```
