import telebot
import os

bot = telebot.TeleBot os.environ ('TELEGRAM_BOT_TOKEN')

ALLOWED_USER_ID = 1066936794  

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != ALLOWED_USER_ID:
        bot.send_message(message.chat.id, "Вибач, ти не маєш доступу до цього бота.")
        return

    text = message.text.strip()
    bot.send_message(message.chat.id, f"Прийнято! Твій текст:\n{text}")

  

bot.polling()