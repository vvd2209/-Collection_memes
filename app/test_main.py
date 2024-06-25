from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_meme():
    response = client.post("/memes/", json={"title": "Test Meme"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"


def test_read_memes():
    response = client.get("/memes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_meme():
    response = client.post("/memes/", json={"title": "Test Meme"})
    meme_id = response.json()["id"]

    response = client.get(f"/memes/{meme_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"


def test_update_meme():
    response = client.post("/memes/", json={"title": "Test Meme"})
    meme_id = response.json()["id"]

    updated_data = {"title": "Updated Meme"}
    response = client.put(f"/memes/{meme_id}", json=updated_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Meme"


def test_delete_meme():
    response = client.post("/memes/", json={"title": "Test Meme"})
    meme_id = response.json()["id"]

    response = client.delete(f"/memes/{meme_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"
