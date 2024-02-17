import time
from typing import Annotated, Any, Dict, List, Literal, Optional
from uuid import uuid4

from pydantic import BaseModel, Field, StringConstraints, conlist


class OpenAIEmbeddingInput(BaseModel):
    input: conlist(  # type: ignore
        Annotated[str, StringConstraints(max_length=8192 * 15, strip_whitespace=True)],
        min_length=1,
        max_length=2048,
    )  # type: ignore
    model: Annotated[str, StringConstraints(min_length=2)]
    user: Optional[str] = None


class _EmbeddingObject(BaseModel):
    object: Literal["embedding"] = "embedding"
    embedding: List[float]
    index: int


class _Usage(BaseModel):
    prompt_tokens: int
    total_tokens: int


class OpenAIEmbeddingResult(BaseModel):
    object: Literal["embedding"] = "embedding"
    data: List[_EmbeddingObject]
    model: str
    usage: _Usage
    id: str = Field(default_factory=lambda: f"infinity-{uuid4()}")
    created: int = Field(default_factory=lambda: int(time.time()))


class RerankInput(BaseModel):
    query: Annotated[
        str, StringConstraints(max_length=1024 * 10, strip_whitespace=True)
    ]
    documents: conlist(  # type: ignore
        Annotated[str, StringConstraints(max_length=1024 * 10, strip_whitespace=True)],
        min_length=1,
        max_length=2048,
    )
    return_documents: bool = False


class _ReRankObject(BaseModel):
    relevance_score: float
    index: int
    document: Optional[str] = None


class ReRankResult(BaseModel):
    object: Literal["rerank"] = "rerank"
    data: List[_ReRankObject]
    model: str
    usage: _Usage
    id: str = Field(default_factory=lambda: f"infinity-{uuid4()}")
    created: int = Field(default_factory=lambda: int(time.time()))


class ModelInfo(BaseModel):
    id: str
    stats: Dict[str, Any]
    object: Literal["model"] = "model"
    owned_by: Literal["infinity"] = "infinity"
    created: int = int(time.time())  # no default factory
    backend: str = ""


class OpenAIModelInfo(BaseModel):
    data: ModelInfo
    object: str = "list"
