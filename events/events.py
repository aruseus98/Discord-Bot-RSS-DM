import discord
from config.config.py import DISCORD_USER_ID, RSS_FEED_URL
from utils.functions.py import get_rss_feed

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        user = await self.fetch_user(DISCORD_USER_ID)
        feed_entries = get_rss_feed(RSS_FEED_URL)

        for entry in feed_entries[:5]:  # Limite à 5 entrées pour l'exemple
            await user.send(f"**{entry.title}**\n{entry.link}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!rss'):
            feed_entries = get_rss_feed(RSS_FEED_URL)
            for entry in feed_entries[:5]:  # Limite à 5 entrées pour l'exemple
                await message.channel.send(f"**{entry.title}**\n{entry.link}")
