import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794  # твій ID

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != ALLOWED_USER_ID:
        return  # якщо ID не співпадає — нічого не відповідаємо

    # якщо ID правильний — тоді виконуємо
    text = message.text.strip()
    bot.send_message(message.chat.id, f"Прийнято! Твій текст:\n{text}")
    # тут далі код для публікації в BlueSky

bot.polling()