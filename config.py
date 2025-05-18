import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20114039"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "87297b8f3cc8fc9bbce591ad30da5896")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "8172163893"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "8172163893").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
