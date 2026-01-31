from fastapi import FastAPI

from app.core.config import settings
from app.db.database import Base, engine
from app.routers.health import router as health_router
from app.routers.patients import router as patients_router

# Simple starter approach: create tables on import
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(health_router)
app.include_router(patients_router)
