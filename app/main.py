from fastapi import FastAPI, HTTPException
import httpx
from app.github_api import fetchRepositoriesFromGitHub

app = FastAPI()

@app.get('/repositories/{username}')
async def getRepositories(username: str):
    """
    Feath public repositories from GitHub for a given username

    Args:
        username (str): GitHub usernamew=

    Raises:
        HTTPException: if user  not found or any  other error.

    Returns:
        List[Repository]: List of Repository  objects
    """
    try:
        repositories = await fetchRepositoriesFromGitHub(username)
        return repositories
    except HTTPException as e:
        raise e