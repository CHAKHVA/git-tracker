import httpx
from fastapi import HTTPException
from collections import Counter


async def get_user_summary(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="GitHub user not found.")
        return response.json()


async def get_user_repos(username: str, limit: int, sort: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}/repos")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Repositories not found.")
        repos = response.json()
        sorted_repos = sorted(repos, key=lambda x: x.get(sort, 0), reverse=True)
        return sorted_repos[:limit]


async def get_user_languages(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}/repos")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Repositories not found.")
        repos = response.json()

    language_counts = Counter()
    for repo in repos:
        if repo["language"]:
            language_counts[repo["language"]] += 1

    total = sum(language_counts.values())
    return {lang: f"{(count / total) * 100:.2f}%" for lang, count in language_counts.items()}


async def get_user_activity(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}/events/public")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Activity not found.")
        return response.json()
