import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi_cache import FastAPICache
from fastapi.responses import ORJSONResponse
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from src.metadata import DESCRIPTION, TAG_METADATA, TITLE, VERSION
from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend
from config import settings
from src.api import router
from loguru import logger


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
    return _app


app = create_fastapi_app()
