import threading
import time
import feedparser
import telebot

from src.config import token
from src.config import NEWS_SOURCES, channel_username


bot = telebot.TeleBot(token)
SENT_NEWS = set()

def get_news():
    """Получение новостей из всех источников"""
    all_news = []

    for source_name, source_url in NEWS_SOURCES.items():
        try:
            feed = feedparser.parse(source_url)
            for entry in feed.entries[:1]:
                news_item = {
                    'title': entry.title,
                    'link': entry.link,
                    'source': source_name,
                    'published': entry.published if hasattr(entry, 'published') else 'Не указано'
                }
                all_news.append(news_item)
        except Exception as e:
            print(f"Ошибка при получении новостей из {source_name}: {e}")

    return all_news

def auto_send_news():
    """Автоматическая отправка новостей каждые 4 часа"""
    while True:
        try:
            print("🔄 Автопроверка новостей...")
            send_news_to_channel()
            time.sleep(2400)
        except Exception as e:
            print(f"Ошибка в автоотправке: {e}")
            time.sleep(300)

def send_news_to_channel():
    """Отправка новостей в канал"""
    try:
        news_items = get_news()

        for news in news_items:
            if news['link'] not in SENT_NEWS:
                message = f"🚀 {news['title']}\n\n"
                message += f"📰 Источник: {news['source']}\n"
                message += f"📅 Дата: {news['published']}\n"
                message += f"🔗 Ссылка: {news['link']}"

                bot.send_message(channel_username, message)
                SENT_NEWS.add(news['link'])
                time.sleep(2)

    except Exception as e:
        print(f"Ошибка отправки: {e}")

auto_thread = threading.Thread(target=auto_send_news, daemon=True)
auto_thread.start()

if __name__ == "__main__":
    print("🤖 Бот запущен!")
    bot.polling(none_stop=True, skip_pending=True)
