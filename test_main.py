from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


# def test_phrase():
#     response = client.get("/phrase/Barak Obama")
#     assert response.status_code == 200
#     assert response.json() == {
#         "result": [
#             "barack hussein obama ii",
#             "bə-rahk hoo-sayn oh-bah-mə",
#             "august",
#             "american politician",
#             "44th president",
#         ]
#     }
