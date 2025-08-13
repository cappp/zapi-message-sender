from utils.logger import get_logger

from models import Contact
from database import SessionLocal

logger = get_logger(__name__)


def get_contacts():
    db = SessionLocal()

    try:
        return db.query(Contact).all()

    except Exception as error:
        logger.exception("Error trying to get contacts")
        raise ValueError("Check if the Contacts table exists in the database")

    finally:
        db.close()
