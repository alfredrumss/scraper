from contextlib import asynccontextmanager
from logging import INFO, basicConfig, getLogger
from typing import AsyncGenerator

from fastapi import FastAPI

from src.contrib.db_setup import create_db
from src.contrib.scraper import scrapper_init
from src.endpoints import product

logger = getLogger(__name__)
basicConfig(level=INFO)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    generator function to handles the lifespan events of the application.
    """
    logger.info("Starting up...")
    create_db()
    logger.info("Initiating scraper...")
    # await scrapper_init()
    yield
    logger.info("Shutting down...")
    logger.info("Finished shutting down.")


def get_app() -> FastAPI:
    """
    Returns a FastAPI application".
    """
    app = FastAPI(title="App Scrapper", lifespan=lifespan)
    app.include_router(product.router)
    return app


app = get_app()
