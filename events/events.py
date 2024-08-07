import discord
from config.config import DISCORD_USER_ID, RSS_FEED_URL
from utils.functions import get_rss_feed

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        user = await self.fetch_user(DISCORD_USER_ID)
        feed_entries = get_rss_feed(RSS_FEED_URL)

        if feed_entries:
            latest_entry = feed_entries[0]
            await user.send(f"**{latest_entry.title}**\n{latest_entry.link}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!rss'):
            feed_entries = get_rss_feed(RSS_FEED_URL)
            if feed_entries:
                latest_entry = feed_entries[0]
                await message.channel.send(f"**{latest_entry.title}**\n{latest_entry.link}")
