from logging import INFO, basicConfig, getLogger
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from src.config import get_settings

log = getLogger(__name__)
basicConfig(level=INFO)


DB_SETTINGS = get_settings()
DATABASE_URL = str(DB_SETTINGS.database_url)

engine = create_engine(DATABASE_URL)


def create_db() -> None:
    """
    Creates the contrib and tables.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, Session, None]:
    """
    Generator for a contrib session to be used in routers.
    Return: Database session generator
    """
    log.info("Initialising contrib session...")
    with Session(engine) as session:
        yield session
