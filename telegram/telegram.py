from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

key = open('keys/key').read().splitlines()[0]


def main():
    updater = Updater(key)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('help', help))
    # dispatcher.add_handler(CommandHandler('unmute', unmute))

    updater.start_polling()
    updater.idle()
