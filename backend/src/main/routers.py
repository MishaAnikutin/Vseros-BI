from fastapi import FastAPI

from src.api import router


def init_routers(app: FastAPI):
    app.include_router(router=router)
