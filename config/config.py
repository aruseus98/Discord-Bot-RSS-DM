import os
from dotenv import load_dotenv
import logging

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))  # Assurez-vous que l'ID du canal est un entier
RSS_FEED_URLS = os.getenv('RSS_FEED_URLS').split(',')

# Création du répertoire logs si nécessaire
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s', filename='logs/bot.log', filemode='a')
