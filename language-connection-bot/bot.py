import telebot
import os
import random
import logging
from datacontroller import get_line
from dotenv import load_dotenv
import csv

load_dotenv()

logging.basicConfig(filename='bot.log', level=logging.INFO)

logger = logging.getLogger('langugage_connection_bot')
logger.setLevel(logging.INFO)
logger.info('bot is started!')

with open('french.csv', 'r', encoding='utf-8') as cfile:
    data = list(csv.reader(cfile))

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "main menu"),
    telebot.types.BotCommand("/help", "print usage"),
    #telebot.types.BotCommand("/settings", "change behaviour"),
    #telebot.types.BotCommand("/stop", "stop the bot"),
    telebot.types.BotCommand("/next", "get the next phrase")
])

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'hi')

@bot.message_handler(commands=['next'])
def dice(message):
    res = get_line(data)
    print(data[0])
    print(res)
    if res:
        bot.reply_to(message, str(res))
    else:
        logger.warning("IT'S EMPTY!!")

@bot.message_handler(commands=['help'])
def help(message):
    commands = bot.get_my_commands()
    response = "Bot commands:\n"
    for command in commands:
        response += f"/{command.command} - {command.description}\n"
    bot.reply_to(message, response)

bot.infinity_polling()
