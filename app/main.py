from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine, Base
from app.api import project_routes, auth_routes
from app.seed.seed import seed_data

app = FastAPI(title="Cloud10: Jira-like Project Manager")

Base.metadata.create_all(bind=engine)
seed_data()

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(project_routes.router, prefix="/api")
