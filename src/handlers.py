from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from main import bot, send_news_to_channel
from src.config import NEWS_SOURCES


@bot.message_handler(commands=['start'])
def start(message):
    """Команда старт"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton('📰 Новости сейчас'),
        KeyboardButton('⚙️ Источники')
    )

    bot.send_message(
        message.chat.id,
        "🤖 Бот для IT-новостей готов к работе!\n\n"
        "Нажмите '📰 Новости сейчас' для получения свежих новостей\n"
        "Или '⚙️ Источники' для просмотра источников",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == '📰 Новости сейчас')
def send_news_now(message):
    """Ручная отправка новостей"""
    bot.send_message(message.chat.id, "🔄 Ищу свежие новости...")
    send_news_to_channel()
    bot.send_message(message.chat.id, "✅ Новости отправлены в канал!")

@bot.message_handler(func=lambda message: message.text == '⚙️ Источники')
def show_sources(message):
    """Показать источники"""
    sources_text = "📚 Используемые источники:\n\n"
    for source in NEWS_SOURCES.keys():
        sources_text += f"• {source}\n"

    bot.send_message(message.chat.id, sources_text)

@bot.message_handler(commands=['news'])
def news_command(message):
    """Команда /news"""
    send_news_now(message)

@bot.message_handler(commands=['sources'])
def sources_command(message):
    """Команда /sources"""
    show_sources(message)
