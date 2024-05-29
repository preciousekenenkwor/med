from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.app import init_app
from app.utils.crud.types_crud import response_message

app = init_app()


# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.on_event("startup")

@app.get('/')
async def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content = response_message(data="welcome to medic", success_status=True, message="success"))