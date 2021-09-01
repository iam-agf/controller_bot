# coding=utf-8
from botRequests import *
import os
import telebot
from modularfunctions.hello_function import helloFunction
from modularfunctions.add_password_function import addPasswordFunction
from modularfunctions.input_command_function import inputCommandFunction

password = None
bot = telebot.TeleBot(token)
os.chdir(os.path.abspath('/home'))

@bot.message_handler(commands = ['start'])
def hello(message):
    helloFunction(message)

@bot.message_handler(commands =["password"])
def addPassword(message):
    global password
    password = addPasswordFunction(message)

@bot.message_handler(func = lambda mess: True)
def inputCommand(message):
    inputCommandFunction(message, password)

bot.polling()