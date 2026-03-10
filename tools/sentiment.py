from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from config import llm

base_dir = Path(__file__).parent.parent
template_text = Path(base_dir / "prompts" / "sentiment_tool").read_text(encoding="utf-8")
prompt_template = PromptTemplate.from_template(template_text)


@tool
def sentiment_tool(comment: str) -> str:
    """
    对评论情感进行简短分析。
    返回：积极|中性|消极，并给出一条理由。
    :param comment:
    :return:
    """
    formatted = prompt_template.format(comment=comment)
    resp = llm.invoke(formatted)
    return resp.content.strip()
