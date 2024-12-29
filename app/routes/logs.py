from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db

router = APIRouter()

@router.get("/")
def get_logs(db: Session = Depends(get_db)):
    logs = db.execute("SELECT * FROM logs").fetchall()
    return {"logs": logs}

