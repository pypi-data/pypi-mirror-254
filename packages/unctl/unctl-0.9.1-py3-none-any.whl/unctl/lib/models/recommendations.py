from dataclasses import field

from pydantic import BaseModel
from typing import List


class LLMRecommendation(BaseModel):
    """Model which reflects recommendation formed from llm response"""

    summary: str = ""
    fixes: List[str] = field(default_factory=list)
    objects: List[str] = field(default_factory=list)
    diagnostics: List[str] = field(default_factory=list)


class GroupLLMRecommendation(BaseModel):
    title: str = ""
    summary: str = ""
    objects: List[str] = field(default_factory=list)
