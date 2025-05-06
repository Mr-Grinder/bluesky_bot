import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794  # заміни на свій ID
ACCESS_PASSWORD = "1234"      # простий пароль
authenticated_users = set()   # ID користувачів, що ввели правильний пароль

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.strip()

    if user_id != ALLOWED_USER_ID:
        return  # ігноруємо інших

    if user_id not in authenticated_users:
        if text == ACCESS_PASSWORD:
            authenticated_users.add(user_id)
            bot.send_message(message.chat.id, "🔓 Доступ надано! Тепер можеш надсилати пости.")
        else:
            bot.send_message(message.chat.id, "🔒 Введи пароль:")
        return

    # користувач вже ввів пароль — приймаємо пости
    bot.send_message(message.chat.id, f"✅ Пост умовно надіслано до BlueSky:\n{text}")
    # сюди вставиш код публікації

bot.polling()
