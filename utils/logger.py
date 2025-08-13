import os
import logging

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT") or "development"
print(f"Executing in {ENVIRONMENT} mode")


def get_logger(name=__name__):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        fh = logging.FileHandler("app.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        ch = logging.StreamHandler()

        if ENVIRONMENT == "development":
            ch.setLevel(logging.DEBUG)

        elif ENVIRONMENT == "production":
            ch.setLevel(logging.INFO)

        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
