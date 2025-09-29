from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import uuid
from datetime import datetime

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
    topic: str

class AnalysisResponse(BaseModel):
    id: str
    text: str
    topic: str
    created_at: str

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(analysis: AnalysisRequest):
    analysis_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    result = {
        "id": analysis_id,
        "text": analysis.text,
        "topic": analysis.topic,
        "created_at": timestamp
    }
    
    analyses[analysis_id] = result
    return result
