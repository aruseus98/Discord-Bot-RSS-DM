import os
from dotenv import load_dotenv
import logging

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_USER_ID = os.getenv('DISCORD_USER_ID')
RSS_FEED_URLS = os.getenv('RSS_FEED_URLS').split(',')

# Création du répertoire logs si nécessaire
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s', filename='logs/bot.log', filemode='a')
