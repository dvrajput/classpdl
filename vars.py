#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24141594"))
API_HASH = environ.get("API_HASH", "43b7aff46f8893496f335018c6723a6d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7454376098:AAGdSn0V5PB_otZ9wTaoOseAiUThAQXUYQk")

OWNER = int(environ.get("OWNER", "1722652154"))
CREDIT = environ.get("CREDIT", "dv1910")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1591043415,1722652154').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1591043415,1722652154').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
