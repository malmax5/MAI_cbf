from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers.handlers import router


app = FastAPI()


app.include_router(router)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')