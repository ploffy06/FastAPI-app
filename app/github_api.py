import httpx
from app.models import Repository
from fastapi import HTTPException

async def fetchRepositoriesFromGitHub(username):
    """
    Fetch public repositories from GitHub API given the username

    Args:
        username (str): GitHub username

    Raises:
         HTTPException: If user not found or any other error occurs.

    Returns:
        List[Repository]: List of Repository  objects containing repository
        name, description, language andnumber ofstars
    """
    try:
        response = httpx.get(f'https://api.github.com/users/{username}/repos')
        response.raise_for_status()

        repos = []
        for repo in response.json():
            repos.append(Repository(
                name=repo['name'],
                description=repo['description'] or '',
                language=repo['language'] or '',
                stars=repo['stargazers_count']
            ))
        return repos
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f'User with username {username} not found.'
            )
        elif e.response.status_code == 500:
            raise HTTPException(status_code=500, detail='Internal Server Error.')