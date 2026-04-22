from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from model_util import Prompt
from model_util.Model import llm_message
from vector_db.VectorDB import db

app = FastAPI()


class DocumentModel(BaseModel):
    page_content: str
    metadata: dict[str, Any] = {}


class RetrieveRequest(BaseModel):
    query: str
    top_k: int


class RetrieveResponse(BaseModel):
    query: str
    documents: list[DocumentModel]


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str

@app.post("/retrieve",response_model=RetrieveResponse)
def get_retrieve(req:RetrieveRequest):
    docs = db.queryDB(req.query,req.top_k)

    document_models = [
        DocumentModel(
            page_content=doc.get("page_content", ""),
            metadata=doc.get("metadata", {})
        )
        for doc in docs
    ]
    return RetrieveResponse(
        query=req.query,
        documents=document_models
    )

@app.post("/summary",response_model=ChatResponse)
def get_summary(req:ChatRequest):
    res = llm_message(Prompt.SUMMARY_PROMPT,req.message)
    return ChatResponse(
        response=res
    )

@app.post("/chat",response_model=ChatResponse)
def get_summary(req:ChatRequest):
    res = llm_message(Prompt.SYSTEM_PROMPT,req.message)
    return ChatResponse(
        response=res
    )

