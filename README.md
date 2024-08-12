# Discord RSS Bot

This project is a Discord bot that monitors one or more RSS feeds and sends notifications for new entries directly to a specific Discord channel.

## 2 Bot version
* Main branch : bot rss DM the user 
* Setup bot to send to channel : bot rss send message to a specific channel in a server discord

## Prerequisites
* Python 3.9 or higher  
* A Discord token  
* Docker (optional)  

## Installation

1. Clone the repository:  
```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install dependencies:  

If you're using a virtual environment, activate it first.  
```
pip install -r requirements.txt
```

3. Configuration:  

Create a .env file at the root of the project and add your information:  
```
DEBUG_MODE=false  # Set to 'true' to enable debug mode loggin
DISCORD_TOKEN=your_discord_token_here
DISCORD_USER_ID=your_user_id_here
RSS_FEED_URL=your_rss_feed_url_here
```

4. Run the bot:  
```
python bot.py
```

## Usage  

Once the bot is running, it will connect to Discord and start monitoring the configured RSS feeds. It will notify the specified channel when new entries are detected.   

Available Commands

* !rss: Displays the latest entry from the RSS feed.  

## Debug Mode

* To enable detailed logging, set DEBUG_MODE=true in your .env file.  
* Logs are stored in the logs directory only when DEBUG_MODE is enabled.  

## Using Docker

1. Build the Docker image:  
```
docker build -t discord-rss-bot .
```

2. Run the container:  
```
docker run -d --name discord-rss-bot --env-file .env discord-rss-bot
```

## Project Structure

* config/config.py: Bot configuration, including logging setup.  
* events/events.py: Handles Discord events (connection, messages, etc.).  
* utils/functions.py: Utility functions for processing RSS feeds.  
* bot.py: Main entry point of the bot.  
* Dockerfile: Configuration file for building a Docker image.  

## Logs

Logs are stored in the logs directory when DEBUG_MODE is enabled, providing detailed information about the bot's execution and actions taken.  