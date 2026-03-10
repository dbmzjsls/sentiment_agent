from pathlib import Path
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from tools.sentiment import sentiment_tool
from tools.risk import risk_tool
from tools.keypoint import keypoint_tool
from config import llm

base_dir = Path(__file__).parent.parent
system_prompt = (base_dir / "prompts" / "agent_system.txt").read_text(encoding="utf-8")

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

# Agent
tools = [sentiment_tool, risk_tool, keypoint_tool]

agent = create_openai_tools_agent(
    llm=llm,
    tools=[sentiment_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[sentiment_tool],
    verbose=True
)

# Memory
store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)
