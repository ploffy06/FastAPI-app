from fastapi import FastAPI, HTTPException
import httpx
from app.github_api import fetchRepositoriesFromGitHub

app = FastAPI()

@app.get('/repositories/{username}')
async def getRepositories(username: str):
    try:
        repositories = await fetchRepositoriesFromGitHub(username)
        return repositories
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code)