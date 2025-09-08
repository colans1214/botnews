import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')
channel_username = os.getenv('CHANNEL_USERNAME')

NEWS_SOURCES = {
    "TJournal Tech": "https://tjournal.ru/rss/tech",
    "TJournal Internet": "https://tjournal.ru/rss/internet",
    "TJournal Science": "https://tjournal.ru/rss/science",
    "3DNews IT": "https://3dnews.ru/news/rss/",
    "3DNews Hardware": "https://3dnews.ru/hardware/rss/",
    "IXBT News": "https://www.ixbt.com/export/news.rss",
    "IXBT Hardware": "https://www.ixbt.com/export/hardnews.rss",
    "Hacker News": "https://news.ycombinator.com/rss",
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge Tech": "https://www.theverge.com/tech/rss/index.xml",
    "Ars Technica": "http://feeds.arstechnica.com/arstechnica/index",
}