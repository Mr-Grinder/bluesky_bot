import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794

def is_allowed(message):
    return message.from_user.id == ALLOWED_USER_ID

@bot.message_handler(func=is_allowed)
def handle_message(message):
    text = message.text.strip()
    bot.send_message(message.chat.id, f"Прийнято! Твій текст:\n{text}")

bot.polling()