import feedparser

def get_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries
