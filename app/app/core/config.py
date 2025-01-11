import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
YANDEX_USER_ID = os.getenv("YANDEX_USER_ID")
YANDEX_HOST_ID = os.getenv("YANDEX_HOST_ID")
