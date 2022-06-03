from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic, search_wiki, phrases as wiki_phrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """
    Page to search wikipedia
    """
    return {"result": search_wiki(value)}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """
    Retrieve wikipedia page
    """
    return {"result": wikilogic(name)}


@app.get("/phrase/{w_phrase}")
async def phrase(w_phrase: str):
    """
    Retrieve wikipedia page and returns phrases
    """
    return {"result": wiki_phrases(w_phrase)}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
