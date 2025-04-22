from pydantic import BaseModel, HttpUrl


class UserSummary(BaseModel):
    login: str
    name: str | None
    followers: int
    following: int
    public_repos: int
    avatar_url: HttpUrl
    html_url: HttpUrl


class RepoItem(BaseModel):
    name: str
    description: str | None
    html_url: HttpUrl
    stargazers_count: int
    language: str | None


class LanguageUsage(BaseModel):
    language: str
    percentage: str


class ActivityItem(BaseModel):
    id: str
    type: str
