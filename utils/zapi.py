import os

from utils.logger import get_logger
from requests import post

logger = get_logger(__name__)

ZAPI_INSTANCE_STRING = os.getenv("ZAPI_INSTANCE_STRING")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")
if not ZAPI_INSTANCE_STRING or not ZAPI_CLIENT_TOKEN:
    logger.error("ZAPI env variables not found")
    raise ValueError(
        "ZAPI_INSTANCE_STRING or ZAPI_CLIENT_TOKEN env variables not defined"
    )


def send_text(phone, message):
    url = f"{ZAPI_INSTANCE_STRING}/send-text"

    headers = {"Client-Token": ZAPI_CLIENT_TOKEN, "Content-Type": "application/json"}

    payload = {"phone": phone, "message": message}

    response = None

    try:
        logger.debug(f"Sending text to {phone}...")

        response = post(url, json=payload, headers=headers)
        response.raise_for_status()

        result = response.json()

        if "error" in result and result["error"]:
            logger.error(f"Error trying to send text to {phone}: {result}")
        else:
            logger.info(f"Text sent successfully to {phone}: {result}")
    except Exception as error:
        logger.exception(f"Exception sending text to {phone}")

        if response is None:
            raise ValueError("Check if the ZAPI_INSTANCE_STRING env variable is valid")

        if response.status_code == 403:
            raise ValueError("Check if the ZAPI_CLIENT_TOKEN env variable is valid")
