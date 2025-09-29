from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import uuid
from datetime import datetime
from llm_summary import get_analysis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

analyses: Dict[str, dict] = {}

class AnalysisRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    id: str = None
    text: str = None
    created_at: str = None

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(analysis: AnalysisRequest):
    summary = get_analysis(analysis.text)
    return {"text": summary}
