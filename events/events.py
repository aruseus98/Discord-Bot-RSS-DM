import discord
import asyncio
import logging
from config.config import DISCORD_CHANNEL_ID, RSS_FEED_URLS
from utils.functions import get_rss_feed, read_last_entry, write_last_entry

class MyBot(discord.Client):
    async def on_ready(self):
        logging.info(f'Logged in as {self.user}')
        print(f'We have logged in as {self.user}')

        self.channel_to_notify = self.get_channel(DISCORD_CHANNEL_ID)
        if self.channel_to_notify is None:
            logging.error(f"Channel with ID {DISCORD_CHANNEL_ID} not found")
        else:
            self.check_rss_task = self.loop.create_task(self.check_rss_feeds())

    async def check_rss_feeds(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for feed_url in RSS_FEED_URLS:
                logging.info("Checking RSS feed: %s", feed_url)
                feed_entries = get_rss_feed(feed_url)
                if feed_entries:
                    latest_entry = feed_entries[0]
                    last_entry_id = await read_last_entry(feed_url)

                    if latest_entry.id != last_entry_id:
                        if self.channel_to_notify:
                            await self.channel_to_notify.send(f"**{latest_entry.title}**\n{latest_entry.link}")
                            await write_last_entry(feed_url, latest_entry.id)
                            logging.info("New entry sent from %s: %s", feed_url, latest_entry.title)
                    else:
                        logging.info("No new entry found for %s.", feed_url)
                else:
                    logging.warning("No entries found in the RSS feed for %s.", feed_url)

            await asyncio.sleep(900)  # Vérifie toutes les 15 minutes

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!rss'):
            logging.info("Received !rss command")
            for feed_url in RSS_FEED_URLS:
                feed_entries = get_rss_feed(feed_url)
                if feed_entries:
                    latest_entry = feed_entries[0]
                    await message.channel.send(f"**{latest_entry.title}**\n{latest_entry.link}")
                    logging.info("Sent latest entry from %s: %s", feed_url, latest_entry.title)
