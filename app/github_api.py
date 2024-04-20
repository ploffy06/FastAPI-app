import httpx
from app.models import Repository

async def fetchRepositoriesFromGitHub(username):
    try:
        response = httpx.get(f'https://api.github.com/users/{username}/repos')
        repos = []
        for repo in response.json():
            repos.append(Repository(
                name=repo['name'],
                description=repo['description'] or '',
                language=repo['language'] or '',
                stars=repo['stargazers_count']
            ))
        return repos
    except httpx.HTTPError as exc:
        raise exc