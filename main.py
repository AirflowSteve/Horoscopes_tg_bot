from info import *
import telebot
from dotenv import load_dotenv
import os
import schedule
from threading import Thread
from time import sleep
import pickle
from user import User
from prophecies.requesting_horoblocks import get_horoscope


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
    global users
    for usr in users.values():
        print(usr.id)


@bot.message_handler(commands=["all_signs"])
def all_signs(message):
    bot.send_message(message.chat.id, ", ".join(signs_zod))


@bot.message_handler(commands=["sign"])
def show_sign(message):
    print(users)
    usr = users.get(message.chat.id)
    if usr is None:
        bot.send_message(message.chat.id, "Такого пользователя пока нет")
    else:
        bot.send_message(message.chat.id, usr.sign)


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
        users[message.chat.id] = User(message.chat.id, sign.capitalize())
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
            bot.send_message(usr, users.get(usr).prophecy)
        except Exception:
            print(Exception)
            deleted = True
    if deleted:
        del users[usr]
        with open("users.bin", "wb") as file:
                    pickle.dump(users, file)
        deleted = False

def creating_prophecies():
    global users
    for id, usr in users.items():
        usr.prophecy = get_horoscope(usr.url)

@bot.message_handler(commands=["гороскоп"])
def send_info(message):
    usr = users.get(message.chat.id)
    if usr:
        bot.send_message(message.chat.id, usr.prophecy)
    else:
        bot.send_message(message.chat.id, "Я пока не знаю кто Вы")

# schedule.every(3).minutes.do(creating_prophecies)

# schedule.every(5).minutes.do(SENDING_FUNCTION)

schedule.every().day.at("10:00:00").do(creating_prophecies)

schedule.every().day.at('10:30:00').do(SENDING_FUNCTION)

Thread(target=schedule_checker).start()

bot.infinity_polling()