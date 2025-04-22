from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="GitTracker API",
    description="Track GitHub user contribution stats and activity.",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")
