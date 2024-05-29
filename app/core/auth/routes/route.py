

from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database.db import get_db, session_manager
from app.core.auth.services.service_auth import AuthService
from app.core.users.services.service_user import UserService
from app.core.users.types.type_user import CreateUserD, CreateUserT

auth_router = APIRouter()

@auth_router.post("/", name="AUTH API", summary="this api end point is responsible for authenticating the user on the platform ")
async def create_user (data:Annotated[CreateUserT, Body()], db:AsyncSession=Depends(get_db)):
    user = AuthService(db=db)
    create_user = await user.create(data={**data})
    jsonn=jsonable_encoder(create_user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonn)