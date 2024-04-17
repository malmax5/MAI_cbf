from fastapi import FastAPI
from fastapi.responses import RedirectResponse

#api
from app.api.schemas.user_articles import UserArticle_Create
from pydantic import constr


app = FastAPI()

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')

@app.post('/user/createArticle')
async def create_article(data: UserArticle_Create):
    try:
        # Logic
        return {"Valid", "Article created"}
    except Exception as ex:
        return {"Invalid creating article", f"{ex}"}

@app.get('/user/allArticles/article')
async def all_articles_by_user_id(user_id: int, article_name: constr(max_length=255)):
    try:
        # Logic
        return {"Valid", "Got all articles"}
    except Exception as ex:
        return {"Invalid getting all articles", f"{ex}"}

@app.get('/user/allArticles')
async def all_articles_by_user_id(user_id: int):
    try:
        # Logic
        return {"Valid", "Got all articles"}
    except Exception as ex:
        return {"Invalid getting all articles", f"{ex}"}