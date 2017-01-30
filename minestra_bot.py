import telebot

bot = telebot.TeleBot(token='277842064:AAFflOSXBvno7qgkHKz9aga09R2xSKJTpDM')


def minestra():
    return open('minestra.png', 'rb')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hai voglia di qualcosa di buono?")


@bot.message_handler(regexp='fame')
def ho_fame(message):
    bot.send_message(message.chat.id, 'Fatti una minestra di Gnappo!')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp='buono')
def buono(message):
    bot.send_message(message.chat.id, 'Le cose più buone sono quelle diy, con lo zenzero e la carota viola.')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp='fallito')
def fallito(message):
    bot.send_message(message.chat.id, 'Ma no, non dire così! Fatti una minestra di Gnappo!')

bot.polling()
