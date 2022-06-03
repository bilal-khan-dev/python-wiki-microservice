from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_wiki():
    response = client.get("/wiki/Barak")
    assert response.status_code == 200
    assert "president" in response.json()["result"]


def test_search_wiki():
    response = client.get("/search/Harry_Potter")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "Harry Potter",
            "Harry Potter (film series)",
            "Harry Potter and the Philosopher's Stone",
            "Harry Potter and the Philosopher's Stone (film)",
            "Harry Potter and the Cursed Child",
            "Harry Potter and the Deathly Hallows – Part 2",
            "Magical creatures in Harry Potter",
            "Magic in Harry Potter",
            "Harry Potter and the Half-Blood Prince (film)",
            "Harry Potter and the Order of the Phoenix (film)",
        ]
    }


def test_phrase():
    response = client.get("/phrase/Barak Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
