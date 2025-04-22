from fastapi import APIRouter

from app.schemas.github_schema import (
    UserSummary,
    RepoItem,
    LanguageUsage,
    ActivityItem,
)
from app.services.github_service import (
    get_user_summary,
    get_user_repos,
    get_user_languages,
    get_user_activity,
)

router = APIRouter()


@router.get("/{username}/summary", response_model=UserSummary)
async def summary(username: str):
    return await get_user_summary(username)


@router.get("/{username}/repos", response_model=list[RepoItem])
async def repos(username: str, limit: int = 5, sort: str = "stargazers_count"):
    return await get_user_repos(username, limit, sort)


@router.get("/{username}/languages", response_model=list[LanguageUsage])
async def languages(username: str):
    lang_dict = await get_user_languages(username)
    return [{"language": lang, "percentage": percent} for lang, percent in lang_dict.items()]


@router.get("/{username}/activity", response_model=list[ActivityItem])
async def activity(username: str):
    return await get_user_activity(username)
