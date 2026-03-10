from pathlib import Path
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm

base_dir = Path(__file__).parent.parent
template_text = Path(base_dir / "prompts" / "risk_tool").read_text(encoding="utf-8")
prompt_template = PromptTemplate.from_template(template_text)


@tool
def risk_tool(comment: str) -> str:
    """
    判断评论是否包含投诉或风险信号。
    如：质量问题、售后纠纷、维权、退款等。
    返回：风险类型列表，若无风险返回“无明显风险”。
    :param comment:
    :return:
    """
    formatted = prompt_template.format(comment=comment)
    resp = llm.invoke(formatted)
    return str(resp).strip()
