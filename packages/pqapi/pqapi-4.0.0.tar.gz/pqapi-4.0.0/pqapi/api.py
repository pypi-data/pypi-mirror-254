import json
from logging import getLogger
from typing import Any, BinaryIO, Dict, Union

import aiohttp
import requests
import tenacity

from .models import AnswerResponse, DocsStatus, QueryRequest, UploadMetadata
from .utils import get_pqa_key, get_pqa_url

logger = getLogger(__name__)
PQA_URL = get_pqa_url()


def coerce_request(query: Union[str, QueryRequest]) -> QueryRequest:
    if isinstance(query, str):
        return QueryRequest(query=query)
    elif isinstance(query, QueryRequest):
        return query
    else:
        raise TypeError("Query must be a string or QueryRequest")


def parse_response(data: Dict[str, Any]) -> AnswerResponse:
    return AnswerResponse(**data)


def upload_file(
    bibliography: str,
    file: BinaryIO,
    metadata: UploadMetadata,
    public: bool = False,
) -> Dict[str, Any]:
    if public:
        if not bibliography.startswith("public:"):
            bibliography = f"public:{bibliography}"
    url = f"{PQA_URL}/api/docs/{bibliography}/upload"

    with requests.Session() as session:
        response = session.post(
            url,
            files=[("file", file)],
            data=dict(metadata=metadata.json()),
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        )
        response.raise_for_status()
        result: Dict[str, Any] = response.json()
        return result


def upload_paper(
    paper_id: str,
    file: BinaryIO,
):
    url = f"{PQA_URL}/db/upload/paper/{paper_id}"
    with requests.Session() as session:
        result = session.post(
            url,
            files=[("file", file)],
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        )
        result.raise_for_status()
        return result


def delete_bibliography(bibliography: str, public: bool = False) -> None:
    if public:
        if not bibliography.startswith("public:"):
            bibliography = f"public:{bibliography}"
    url = f"{PQA_URL}/db/docs/delete/{bibliography}"
    with requests.Session() as session:
        response = session.get(
            url,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        )
        response.raise_for_status()


async def async_delete_bibliography(bibliography: str, public: bool = False) -> None:
    if public:
        if not bibliography.startswith("public:"):
            bibliography = f"public:{bibliography}"
    url = f"{PQA_URL}/db/docs/delete/{bibliography}"
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        ) as response:
            response.raise_for_status()


def get_bibliography(bibliography: str, public: bool = False) -> DocsStatus:
    if public:
        if not bibliography.startswith("public:"):
            bibliography = f"public:{bibliography}"
    url = f"{PQA_URL}/api/docs/status/{bibliography}"
    with requests.Session() as session:
        response = session.get(
            url,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        )
        response.raise_for_status()
        result = DocsStatus(**response.json())
        return result


async def async_get_bibliography(bibliography: str, public: bool = False) -> DocsStatus:
    if public:
        if not bibliography.startswith("public:"):
            bibliography = f"public:{bibliography}"
    url = f"{PQA_URL}/api/docs/status/{bibliography}"
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        ) as response:
            data = await response.json()
            result = DocsStatus(**data)
            return result


@tenacity.retry(
    wait=tenacity.wait_random_exponential(multiplier=1, max=30),
    stop=tenacity.stop_after_attempt(3),
)
def agent_query(
    query: Union[QueryRequest, str], bibliography: str = "tmp"
) -> AnswerResponse:
    query_request = coerce_request(query)
    url = f"{PQA_URL}/api/agent/{bibliography if bibliography else 'tmp'}"
    with requests.Session() as session:
        qd = query_request.dict()
        response = session.post(
            url,
            json={"query": qd},
            headers={
                "Authorization": f"Bearer {get_pqa_key()}",
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        response.raise_for_status()
        result = parse_response(response.json())
    return result


@tenacity.retry(
    wait=tenacity.wait_random_exponential(multiplier=1, max=10),
    stop=tenacity.stop_after_attempt(2),
)
async def async_agent_query(
    query: Union[QueryRequest, str],
    bibliography: str = "tmp",
) -> AnswerResponse:
    query_request = coerce_request(query)
    url = f"{PQA_URL}/api/agent/{bibliography if bibliography else 'tmp'}"
    async with aiohttp.ClientSession() as session:
        qd = query_request.dict()
        async with session.post(
            url,
            json={"query": qd},
            timeout=1200,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        ) as response:
            try:
                data = await response.json()
            except Exception:
                text = await response.text()
                logger.warning("Failed Request: \n" + json.dumps(qd, indent=2))
                logger.warning("\n\nResponse:\n\n" + text)
            response.raise_for_status()
            result = parse_response(data)
    return result


@tenacity.retry(
    wait=tenacity.wait_random_exponential(multiplier=1, max=10),
    stop=tenacity.stop_after_attempt(3),
)
async def async_query(
    query: Union[QueryRequest, str], bibliography: str
) -> AnswerResponse:
    query_request = coerce_request(query)
    url = f"{PQA_URL}/api/query/{bibliography}"
    async with aiohttp.ClientSession() as session:
        qd = query_request.dict()
        async with session.post(
            url,
            json=qd,
            timeout=600,
            headers={"Authorization": f"Bearer {get_pqa_key()}"},
        ) as response:
            data = await response.json()
            response.raise_for_status()
            result = parse_response(data)
    return result
