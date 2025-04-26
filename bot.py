import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

ALLOWED_USER_ID = 1066936794  

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    text = message.text.strip()
    
    print(f"Повідомлення від {first_name} (@{username}), ID: {user_id} — {text}")

    if user_id != ALLOWED_USER_ID:
        return  #Просто ігноруємо 

    bot.send_message(message.chat.id, f"Прийнято! Твій текст:\n{text}")

bot.polling()