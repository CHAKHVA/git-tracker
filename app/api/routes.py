from fastapi import APIRouter
from app.api.endpoints import github

router = APIRouter()
router.include_router(github.router, prefix="/users", tags=["GitHub User"])
