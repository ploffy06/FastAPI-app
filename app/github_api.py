import httpx

async def fetchRepositoriesFromGitHub(username):
    try:
        response = await httpx.get(f'https://api.github.com/users/{username}/repos')
        return response.json()
    except httpx.HTTPError as exc:
        raise exc