import pytest
from fastapi.testclient import TestClient
from unittest import mock
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_user_summary_success():
    mock_user_data = {
        "login": "testuser",
        "name": "Test User",
        "followers": 100,
        "following": 50,
        "public_repos": 30,
        "avatar_url": "https://example.com/avatar.png",
        "html_url": "https://github.com/testuser"
    }

    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_user_data

    mock_client = mock.AsyncMock()
    mock_client.__aenter__.return_value.get.return_value = mock_response

    with mock.patch('httpx.AsyncClient', return_value=mock_client):
        response = client.get("/api/users/testuser/summary")

        assert response.status_code == 200
        data = response.json()
        assert data["login"] == "testuser"
        assert data["name"] == "Test User"
        assert data["followers"] == 100
        assert data["following"] == 50
        assert data["public_repos"] == 30
        assert data["avatar_url"] == "https://example.com/avatar.png"
        assert data["html_url"] == "https://github.com/testuser"

@pytest.mark.asyncio
async def test_user_summary_not_found():
    mock_response = mock.Mock()
    mock_response.status_code = 404

    mock_client = mock.AsyncMock()
    mock_client.__aenter__.return_value.get.return_value = mock_response

    with mock.patch('httpx.AsyncClient', return_value=mock_client):
        response = client.get("/api/users/nonexistentuser/summary")

        assert response.status_code == 404
        assert response.json() == {"detail": "GitHub user not found."}
