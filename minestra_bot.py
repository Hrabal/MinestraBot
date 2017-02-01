import telebot
import re
import random

bot = telebot.TeleBot(token='277842064:AAFflOSXBvno7qgkHKz9aga09R2xSKJTpDM')

gnappate = [
    'Io e tizie scopate',
    'Mai una gioia',
    'Scrivi a stocazzo@staminchia.gnappobesutti',
    'pew pew pew, che entusiasmo',
    'Non capire is the new non capire',
    'Aaaaaawww!',
]

def minestra():
    return open('minestra.png', 'rb')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hai voglia di qualcosa di buono?")


@bot.message_handler(regexp=re.compile(r'fame', re.I))
def ho_fame(message):
    bot.send_message(message.chat.id, 'Fatti una minestra di Gnappo!')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'buono', re.I))
def buono(message):
    bot.send_message(message.chat.id, 'Le cose più buone sono quelle diy, con lo zenzero e la carota viola.')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'fallito', re.I))
def fallito(message):
    bot.send_message(message.chat.id, 'Ma no, non dire così! Fatti una minestra di Gnappo!')


@bot.message_handler(regexp=re.compile(r'gnappo', re.I))
def fallito(message):
    bot.send_message(message.chat.id, random.choice(gnappate))

bot.polling()
