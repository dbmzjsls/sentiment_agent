import pandas as pd
from agent.opinion_agent import agent_with_chat_history
from config import ANALYSIS_COUNT

csv_path = 'data/auto-home-comments.csv'
df = pd.read_csv(csv_path, encoding="utf-8", low_memory=False)

# 截取评论条数
test_df = df.head(ANALYSIS_COUNT).copy().reset_index(drop=True)

# 实现多条评论分析
storage = []
for index, row in test_df.iterrows():
    print(f"正在处理第{index + 1}/{ANALYSIS_COUNT}条评论...")
    print(f"评论内容为：{row['评论内容']}")
    # 进行分析
    result = agent_with_chat_history.invoke(
        {"input": f"分析评论内容：\n{row['评论内容']}"},
        config={"configurable": {"session_id": "auto_home_001"}}
    )
    # 提取结果并打印
    output = str(result["output"]).strip()
    storage.append(output)
    print(f"情感分析结果为：{output}")

# 将结果存入 DataFrame
test_df["分析结果"] = storage
test_df.to_csv("data/analyzed_results.csv",
               index=False,
               encoding='utf-8-sig')
