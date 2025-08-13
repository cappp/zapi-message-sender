import os

from utils.logger import get_logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = get_logger(__name__)

DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")
if not DATABASE_CONNECTION_STRING:
    logger.error("DATABASE_CONNECTION_STRING not found in the env variables")
    raise ValueError("DATABASE_CONNECTION_STRING env variable not defined")

try:
    logger.debug("Connecting to the database...")

    engine = create_engine(DATABASE_CONNECTION_STRING)
    SessionLocal = sessionmaker(bind=engine)

    logger.debug("Database connected!")
except Exception as error:
    logger.exception("Error creating engine or sessionmaker for the database")
    raise ValueError("Check if the DATABASE_CONNECTION_STRING env variable is valid")
