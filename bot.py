import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794

@bot.message_handler(func=lambda message: message.from_user.id == ALLOWED_USER_ID)
def handle_message(message):
    text = message.text.strip()
    bot.send_message(message.chat.id, f"✅ Прийнято! Твій текст:\n{text}")

@bot.message_handler(func=lambda message: message.from_user.id != ALLOWED_USER_ID)
def handle_unauthorized(message):
    bot.send_message(message.chat.id, "⛔️ Вибач, у тебе немає доступу до цього бота.")

bot.polling()