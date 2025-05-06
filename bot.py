import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794  # заміни на свій реальний ID

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    print(f"Отримано повідомлення від ID: {user_id}")  # для логів
    if user_id != ALLOWED_USER_ID:
        bot.send_message(message.chat.id, "Вибач, але ти не маєш доступу до цього бота.")
        return

    text = message.text.strip()
    bot.send_message(message.chat.id, f"Прийнято! Твій текст:\n{text}")
