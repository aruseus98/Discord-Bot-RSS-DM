import feedparser
import aiofiles
import os
import logging

LAST_ENTRY_DIR = 'last_entry'

# Assurer la création du répertoire last_entry
if not os.path.exists(LAST_ENTRY_DIR):
    os.makedirs(LAST_ENTRY_DIR)

def get_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

async def read_last_entry(feed_url):
    file_path = os.path.join(LAST_ENTRY_DIR, f"{hash(feed_url)}.txt")
    try:
        async with aiofiles.open(file_path, 'r') as file:
            last_entry = await file.read()
            logging.info("Read last entry for %s: %s", feed_url, last_entry.strip())
            return last_entry.strip()
    except FileNotFoundError:
        logging.warning("Last entry file for %s not found.", feed_url)
        return None

async def write_last_entry(feed_url, entry_id):
    file_path = os.path.join(LAST_ENTRY_DIR, f"{hash(feed_url)}.txt")
    async with aiofiles.open(file_path, 'w') as file:
        await file.write(entry_id)
        logging.info("Wrote last entry for %s: %s", feed_url, entry_id)
