from utils.logger import get_logger
from utils.zapi import send_text

from repositories.contact_repository import get_contacts

if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.debug("Getting contacts from the database...")

    contacts = get_contacts()

    if contacts:
        logger.debug("Got the contacts!")
        logger.debug("Sending text message to all the contacts now...")

        for contact in contacts:
            send_text(contact.phone, f"Olá {contact.name}, tudo bem com você?")
    else:
        logger.warning("There are no contacts in the Contacts table")
