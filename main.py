from info import *
import telebot
from dotenv import load_dotenv
import os
import schedule
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
import requests



load_dotenv(dotenv_path="key.env")
TOKEN = os.environ.get("API_KEY")
bot = telebot.TeleBot(TOKEN)

print("The bot is running! Check it out on https://t.me/Horoscope_cifra_bot")


# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         sleep(1)

@bot.message_handler(content_types=["text"])
def reply(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start', 'help'])
def help_command(message):
    bot.send_message(message.chat.id, HELP)



# @bot.message_handler(commands=["intro"])
# def set_sign(message):




# @bot.message_handler(commands=["intro"])
# def set_sign(message):
#     try:
#         _, sign = message.text.split()
#     except Exception:
#         print(Exception)
#         bot.send_message(message.chat.id, "Неверный формат ввода (/intro <Ваш знак зодиака>)")
#         return
#     if sign.capitalize() in signs_zod:
#         users[message.chat.id] = sign
#         bot.send_message(message.chat.id, "Услышал тебя")
#         with open("usrs_lst.bin", "wb") as f:
#             pickle.dump(users, f)
#         print(users)
#     else:
#         bot.send_message(message.chat.id, "Я таких знаков не знаю")

# @bot.message_handler(commands=["sign"])
# def get_sign(message):
#     bot.send_message(message.chat.id, f"{users.get(message.chat.id, "Мы еще не знакомы")}")


# @bot.message_handler(commands=['clear'])
# def clear_lst(message):
#     users.clear()
#     with open("usrs_lst.bin", "wb") as f:
#             pickle.dump(users, f)
#     bot.send_message(message.chat.id, "Список пользователей очищен")


# schedule.every().minute.do(SENDING_FUNCTION)

# Thread(target=schedule_checker).start()

bot.infinity_polling()