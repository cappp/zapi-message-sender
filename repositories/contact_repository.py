from models import Contact
from database import SessionLocal
from utils.logger import get_logger

logger = get_logger(__name__)

def get_contacts():
  db = SessionLocal()
  
  try:
    return db.query(Contact).all()
  
  except Exception as error:
    logger.exception("Error trying to get contacts") 
    raise ValueError("Check if the table exists in the database")

  finally:
    db.close()
