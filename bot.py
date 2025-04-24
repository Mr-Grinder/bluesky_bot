import os
import telebot
import requests

TELEGRAM_BOT_TOKEN = os.environ.get('7987327814:AAHuVudS4MoOpc4QlA832wEZF2rwC2_KnLI')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def post_to_bluesky(content):
    print(f"I bless everyone who reads this post: {content}")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Надішли мені текст, і я опублікую його в BlueSky.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    content = message.text
    post_to_bluesky(content)
    bot.send_message(message.chat.id, "Пост надіслано в BlueSky (умовно).")

bot.polling()
