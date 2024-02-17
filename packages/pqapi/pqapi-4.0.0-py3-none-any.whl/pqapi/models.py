import re
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import paperqa
import requests
from paperqa.types import Answer, PromptCollection
from pydantic import BaseModel, Field, ValidationInfo, field_validator, validator

from .utils import get_pqa_key, get_pqa_url


class AgentPromptCollection(BaseModel):
    agent_prompt: str = ""
    agent_search_tool: str = ""
    search_count: int = 8
    wipe_context_on_answer_failure: bool = True
    timeout: float = 500  # seconds


def _extract_doi(citation: str) -> Optional[str]:
    doi = re.findall(r"10\.\d{4}/\S+", citation, re.IGNORECASE)
    if len(doi) > 0:
        return doi[-1]
    return None


# we have to put it here to avoid circular imports
# because we use this in the default factory of the QueryRequest
@lru_cache(maxsize=10)
def get_prompts() -> Tuple[Dict[str, PromptCollection], AgentPromptCollection]:
    url = f"{get_pqa_url()}/api/prompts/all"
    with requests.Session() as session:
        response = session.get(
            url,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        )
        response.raise_for_status()
        result = response.json()
    return (
        {
            k: PromptCollection.parse_obj(v["prompt-collection"])
            for k, v in result.items()
        },
        AgentPromptCollection.parse_obj(result["default"]["agent-prompt"]),
    )


class UploadMetadata(BaseModel):
    filename: str
    citation: str
    key: Optional[str] = None


class Doc(paperqa.Doc):
    doi: Optional[str] = None

    @validator("doi", pre=True)
    def citation_to_doi(cls, v: Optional[str], values: Dict) -> Optional[str]:
        if v is None and "citation" in values:
            return _extract_doi(values["citation"])
        return v


class DocsStatus(BaseModel):
    name: str
    llm: str
    summary_llm: str
    docs: List[Doc]
    doc_count: int
    writeable: bool = False


# COPIED FROM paperqa-sverer!
class QueryRequest(BaseModel):
    query: str
    llm: str = "gpt-4"
    summary_llm: str = "gpt-3.5-turbo-1106"
    length: str = "about 200 words, but can be longer if necessary"
    summary_length: str = "100 to 200 words"
    max_sources: int = 7
    consider_sources: int = 12
    named_prompt: Optional[str] = None
    # if you change this to something other than default
    # modify code below in update_prompts
    prompts: PromptCollection = Field(
        default_factory=lambda: get_prompts()[0]["default"], validate_default=True
    )
    agent_tools: AgentPromptCollection = Field(default_factory=lambda: get_prompts()[1])

    @field_validator("max_sources")
    def max_sources_for_gpt(cls, v: int, info: ValidationInfo) -> int:
        values = info.data
        if "gpt" in values["llm"] and v > 10:
            raise ValueError("Max sources for GPT models is 10")
        return v

    @field_validator("prompts")
    def update_prompts(
        cls,
        v: PromptCollection,
        info: ValidationInfo,
    ) -> PromptCollection:
        STATIC_PROMPTS, _ = get_prompts()
        values = info.data
        if values["named_prompt"] is not None:
            if values["named_prompt"] not in STATIC_PROMPTS:
                raise ValueError(
                    f"Named prompt {values['named_prompt']} not in {list(STATIC_PROMPTS.keys())}"
                )
            v = STATIC_PROMPTS[values["named_prompt"]]
        if values["summary_llm"] == "none":
            v.skip_summary = True
            # for simplicity (it is not used anywhere)
            # so that Docs doesn't break when we don't have a summary_llm
            values["summary_llm"] = "gpt-3.5-turbo"
        return v


class AnswerResponse(BaseModel):
    answer: Answer
    usage: Dict[str, List[int]]
    bibtex: Dict[str, str]
    status: str
