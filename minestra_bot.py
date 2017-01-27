import telebot

bot = telebot.TeleBot(token='277842064:AAFflOSXBvno7qgkHKz9aga09R2xSKJTpDM')


REGS = {
    'FAME': r'fame'
}


def send_minestra(bot, chat_id):
    with open('minestra.png', 'rb') as minestra:
        bot.send_photo(chat_id, minestra)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hai voglia di qualcosa di buono?")


@bot.message_handler(regexp='fame')
def ho_fame(message):
    bot.send_message(message.chat.id, 'Fatti una minestra di Gnappo!')
    send_minestra(bot, message.chat.id)


@bot.message_handler(regexp='buono')
def buono(message):
    bot.send_message(message.chat.id, 'Le cose più buone sono quelle diy, con lo zenzero e la carota viola.')
    send_minestra(bot, message.chat.id)


@bot.message_handler(regexp='fallito')
def fallito(message):
    bot.send_message(message.chat.id, 'Fatti una minestra di Gnappo!')

bot.polling()
