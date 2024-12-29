from fastapi import APIRouter, HTTPException
from app.utils.analyzer import analyze_url

router = APIRouter()

@router.get("/")
def analyze_url_route(url: str):
    result = analyze_url(url)
    if not result:
        raise HTTPException(status_code=400, detail="URL analysis failed")
    return result
