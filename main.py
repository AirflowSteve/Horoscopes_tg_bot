from info import *
import telebot
from dotenv import load_dotenv, dotenv_values
import os
import schedule
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
import requests
import pickle


load_dotenv(dotenv_path="key.env")
TOKEN = os.environ.get("API_KEY")
bot = telebot.TeleBot(TOKEN)

print("The bot is running! Check it out on https://t.me/Horoscope_cifra_bot")

try:
    with open("users.bin", "rb") as file:
        users = pickle.load(file)
except Exception:
    print(Exception)
    users = {}


@bot.message_handler(commands=["check"])
def check(message):
    print(users)


@bot.message_handler(commands=["all_signs"])
def all_signs(message):
    bot.send_message(message.chat.id, ", ".join(signs_zod))


@bot.message_handler(commands=["sign"])
def show_sign(message):
    print(users)
    bot.send_message(message.chat.id, users.get(message.chat.id, "Такого пользователя пока нет"))


@bot.message_handler(commands=["intro"])
def set_sign(message):

    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Incorrect format! '/intro *your sign*'")
        return

    try:
        _, sign, _ = message.text.split()
    except ValueError:
        _, sign = message.text.split()

    if sign.capitalize() in signs_zod:
        users[message.chat.id] = sign.capitalize()
        with open("users.bin", "wb") as file:
            pickle.dump(users, file)
        bot.send_message(message.chat.id, "Хорошо, запомнил")
    else:
        bot.send_message(message.chat.id, "Я таких знаков не знаю :(")


@bot.message_handler(commands=['start', 'help'])
def help_command(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['clear'])
def clear_lst(message):
    if message.chat.id == 761232029:
        users.clear()
        with open("users.bin", "wb") as f:
                pickle.dump(users, f)
        bot.send_message(message.chat.id, "Список пользователей очищен")
    else:
        bot.send_message(message.chat.id, "You don't have the authority to do so")



def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def SENDING_FUNCTION():
    global users
    for usr in users:
        deleted = False
        try:
            bot.send_message(usr, users.get(usr))
        except Exception:
            print(Exception)
            deleted = True
    if deleted:
        del users[usr]
        with open("users.bin", "wb") as file:
                    pickle.dump(users, file)
        deleted = False


schedule.every().day.at('10:15:00').do(SENDING_FUNCTION)

Thread(target=schedule_checker).start()

bot.infinity_polling()