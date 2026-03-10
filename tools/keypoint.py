from pathlib import Path
from langchain_core.prompts import PromptTemplate
from config import llm
from langchain.tools import tool

# 读取keypoint_tool
base_dir = Path(__file__).parent.parent
template_text = Path(base_dir / "prompts" / "keypoint_tool").read_text(encoding="utf-8")
prompt_template = PromptTemplate.from_template(template_text)


@tool
def keypoint_tool(comment: str) -> str:
    """
    提取评论中的核心观点或用户最关心的问题。
    返回一句简要总结。
    :param comment:
    :return:
    """
    formatted = prompt_template.format(comment=comment)
    resp = llm.invoke(formatted)
    return str(resp).strip()
