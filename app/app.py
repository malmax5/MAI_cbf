from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')