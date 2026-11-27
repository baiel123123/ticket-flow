from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from .core.database import get_async_session

app = FastAPI()

SessionInjection = Annotated[AsyncSession, Depends(get_async_session)]


@app.get("/health")
async def health(session: SessionInjection):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "okay baby"}
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="huesos")  

