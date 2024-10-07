import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from loguru import logger
from redis import asyncio as aioredis

from config import settings
from src.api import router
from src.api.structure.v1.routers import struct_router
from src.api.tasks.v1.routers import task_router
from src.api.users.v1.routers import (
    auth_router,
    company_reg_router,
    member_reg_router,
    work_data_router,
)
from src.metadata import DESCRIPTION, TAG_METADATA, TITLE, VERSION


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    logger.info("Start redis cache")
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf-8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    yield
    await redis.close()
    logger.info("Shutdown redis cache")


def create_fastapi_app():
    load_dotenv(find_dotenv(".env"))
    env_name = os.getenv("MODE", "DEV")

    if env_name != "PROD":
        _app = FastAPI(
            default_response_class=ORJSONResponse,
            title=TITLE,
            description=DESCRIPTION,
            version=VERSION,
            openapi_tags=TAG_METADATA,
            lifespan=lifespan,
        )
    else:
        _app = FastAPI(
            default_response_class=ORJSONResponse,
            title=TITLE,
            description=DESCRIPTION,
            version=VERSION,
            openapi_tags=TAG_METADATA,
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
        )

    _app.include_router(router=router, prefix="/api")
    _app.include_router(router=auth_router, prefix="/api/auth")
    _app.include_router(router=company_reg_router, prefix="/api")
    _app.include_router(router=member_reg_router, prefix="/api")
    _app.include_router(router=work_data_router, prefix="/api")
    _app.include_router(router=task_router, prefix="/api")
    _app.include_router(router=struct_router, prefix="/api")
    return _app


app = create_fastapi_app()
