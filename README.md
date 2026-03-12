# 舆情评论分析 Agent

基于 LangChain 的智能评论分析系统,用于自动化分析汽车之家用户评论的情感倾向、风险信号和核心观点。

## 项目简介

本项目是一个基于 LangChain Agent 架构的舆情分析工具,能够批量处理用户评论数据,自动识别情感倾向、潜在风险和关键观点,帮助快速了解用户反馈和舆情动态。

## 核心功能

- **情感分析**: 判断评论的情感倾向(积极/中性/消极),并给出置信度和理由
- **风险检测**: 识别评论中的投诉、质量问题、售后纠纷、维权等风险信号
- **观点提取**: 提取评论中的核心观点和用户最关心的问题
- **批量处理**: 支持批量分析 CSV 格式的评论数据
- **对话记忆**: 基于会话历史的上下文理解能力

## 技术栈

- **LangChain**: Agent 框架和工具编排
- **DeepSeek R1**: 大语言模型(通过 OpenAI 兼容接口)
- **Pandas**: 数据处理和分析
- **Python 3.12+**: 开发语言

## 项目结构

```
sentiment_agent/
├── agent/
│   └── opinion_agent.py      # Agent 核心逻辑和配置
├── data/
│   ├── auto-home-comments.csv    # 原始评论数据
│   └── analyzed_results.csv      # 分析结果输出
├── prompts/
│   ├── agent_system.txt      # Agent 系统提示词
│   ├── sentiment_tool        # 情感分析工具提示词
│   ├── risk_tool            # 风险检测工具提示词
│   └── keypoint_tool        # 观点提取工具提示词
├── tools/
│   ├── sentiment.py         # 情感分析工具
│   ├── risk.py             # 风险检测工具
│   └── keypoint.py         # 观点提取工具
├── config.py               # 配置文件
├── main.py                # 主程序入口
├── requirements.txt       # 依赖列表
└── .env                  # 环境变量配置
```

## 安装步骤

1. 克隆项目到本地
```bash
git clone <repository-url>
cd sentiment_agent
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量

创建 `.env` 文件并配置以下内容:
```env
DASHSCOPE_API_KEY=your_api_key_here
DASHSCOPE_BASE_URL=your_base_url_here
```

## 使用方法

### 1. 准备数据

将待分析的评论数据放入 `data/auto-home-comments.csv` 文件中,确保包含 `评论内容` 列。

### 2. 配置分析数量

在 `config.py` 中设置要分析的评论数量:
```python
ANALYSIS_COUNT = 50  # 修改为需要分析的评论条数
```

### 3. 运行分析

```bash
python main.py
```

### 4. 查看结果

分析完成后,结果将保存在 `data/analyzed_results.csv` 文件中。

## 输出格式

分析结果为 JSON 格式,包含以下字段:

```json
{
  "sentiment": "positive | neutral | negative",
  "confidence": 0.0,
  "reason": "不超过30字的中文原因"
}
```

## 工具说明

### sentiment_tool (情感分析工具)
- 功能: 分析评论的情感倾向
- 输出: 积极/中性/消极 + 理由

### risk_tool (风险检测工具)
- 功能: 识别投诉、质量问题、售后纠纷等风险信号
- 输出: 风险类型列表或"无明显风险"

### keypoint_tool (观点提取工具)
- 功能: 提取评论核心观点
- 输出: 一句简要总结

## 依赖项

- langchain
- langchain-openai
- python-dotenv~=1.2.1
- pandas~=3.0.1

## 注意事项

1. 确保 API Key 和 Base URL 配置正确
2. 评论数据需要包含 `评论内容` 列
3. 大批量分析时注意 API 调用频率限制
4. 建议先用小批量数据测试效果

## 开发说明

### 添加新工具

1. 在 `tools/` 目录下创建新的工具文件
2. 使用 `@tool` 装饰器定义工具函数
3. 在 `prompts/` 目录下创建对应的提示词文件
4. 在 `agent/opinion_agent.py` 中注册新工具

### 修改提示词

编辑 `prompts/` 目录下的对应文件即可,无需修改代码。

## License

MIT
