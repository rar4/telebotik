import telegram.ext.filters
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint

TOKEN = '5173101685:AAFrk3qPm3vV2ZIELv31ogyrkjlPzjWOdiY'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
print('Bot started.')
def start(update, context):
    chat = update.effective_chat
    a = 'Hello, welcome to calculator bot, input a quotation please'
    context.bot.send_message(chat_id=chat.id, text=a)


def ca(s, b, action):
    if action == "+":
        f = s + b
        if f % 1 == 0:
            f = int(f)
    elif action == "-":
        f = s - b
        if f % 1 == 0:
            f = int(f)
    elif action == "*":
        f = s * b
        if f % 1 == 0:
            f = int(f)
    elif action == "/":
        if b!= 0:
            f = s / b
        else:
