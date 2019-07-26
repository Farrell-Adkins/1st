#pip install python-telegram-bot==12.0.0b1

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


updater = Updater(token='933096366:AAELflDznr7UEiSIYhi__eC2dyZ_-kKihQs', use_context=True)
dispatcher = updater.dispatcher

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand what you want :|")
unknown_handler = MessageHandler(Filters.text, unknown)
dispatcher.add_handler(unknown_handler)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a webcubers bot, if you want teach you development press start ...")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# import requests

# btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/').json()
# print(f"Price for 1 BTC is {str(btc[0]['price_usd'])}$")

# updater.start_polling()