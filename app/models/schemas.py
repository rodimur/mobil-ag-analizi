from pydantic import BaseModel

class URLAnalysisRequest(BaseModel):
    url: str

class URLAnalysisResponse(BaseModel):
    url: str
    status: str
