import pytest
from fastapi.testclient  import TestClient
from app.main  import app

client = TestClient(app)

@pytest.mark.asyncio
async def testGetRepositoriesSuccess():
    valid_username = 'google'
    response = client.get(f'/repositories/{valid_username}')
    assert response.status_code ==  200

@pytest.mark.asyncio
async def testGetRepositoriesUserNotFound():
    invalid_username = 'opwiefjfoweijf'
    response = client.get(f'/repositories/{invalid_username}')
    print("IOWUEFHOEIW HGERE")
    print(response)
    assert response.status_code == 404
