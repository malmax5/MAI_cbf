import json

from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import constr

from app.schemas.user_articles import UserArticle_Create
from app.database import get_async_session, get_user_subs, get_user_publics
from app.models.models_articles import publics
from app.models.models_stats import articles

router = APIRouter(
    prefix="/articles",
    tags=["Article"]
)

@router.get('/testdb')
async def db_session_test(session: AsyncSession() = Depends(get_async_session)):
    return await get_user_publics(session)
