import pytest
from fastapi.testclient  import TestClient
from app.main  import app

client = TestClient(app)

@pytest.mark.asyncio
async def testGetRepositoriesSuccess():
    valid_username = 'google'
    response = client.get(f'/repositories/{valid_username}')

    assert response.status_code ==  200
    repositories = response.json()

    assert isinstance(repositories, list)
    assert all('name' in repo for repo in repositories)
    assert all('description' in repo for repo in repositories)
    assert all('language' in repo for repo in repositories)
    assert all('stars' in repo for repo in repositories)

@pytest.mark.asyncio
async def testGetRepositoriesUserNotFound():
    invalid_username = 'opwiefjfoweijf'
    response = client.get(f'/repositories/{invalid_username}')

    assert response.status_code == 404
