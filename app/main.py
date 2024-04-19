from fastapi import FastAPI
from github_api import fetchRepositoriesFromGitHub

app = FastAPI()

@app.get('/repositories/{username}')
async def getRepositories(username: str):
    try:
        repositories = fetchRepositoriesFromGitHub(username)
        return reposotories
    except:
        return 0