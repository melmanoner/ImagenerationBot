import os
from dotenv import load_dotenv

dotenv_path =os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TELEGRAM_TOKEN')
AI_KEY = os.environ.get('AI_KEY')

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
BOT_ADMIN = os.environ.get('BOT_ADMIN')