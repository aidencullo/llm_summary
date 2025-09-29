from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Dict, Optional
import uuid
from datetime import datetime

app = FastAPI()

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

@app.get("/search", response_model=List[AnalysisResponse])
async def search_analyses(topic: str = Query(..., description="Topic to search for")):
    matching_analyses = [
        analysis for analysis in analyses.values() 
        if topic.lower() in analysis["topic"].lower()
    ]
    return matching_analyses
