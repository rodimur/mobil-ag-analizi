from fastapi import FastAPI
from app.routes import vpn, logs
from app.routes import threat
from app.config.settings import API_KEY
from app.routes import vpn, logs


app = FastAPI(title="Mobil Ağ Trafiği Analizi")
@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Mobil Ağ Trafiği Analizi API'si Çalışıyor!",
        "docs_url": "http://127.0.0.1:8000/docs",
        "redoc_url": "http://127.0.0.1:8000/redoc"
    }
# Rotaları ekleme
app.include_router(threat.router, prefix="/threats", tags=["Threat Analysis"])
app.include_router(vpn.router, prefix="/vpn", tags=["VPN Management"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


