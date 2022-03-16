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
            f = 'you shouldn`t do like this with zero'
            return f
        if f % 1 == 0:
            f = int(f)
    elif action == "//":
        if b!= 0:
            f = s // b
        else:
            f = 'you shouldn`t do like this with zero'
            return f
        if f % 1 == 0:
            f = int(f)
    elif action == "%":
        if b!= 0:
            f = s % b
        else:
            f = 'you shouldn`t do like this with zero'
            return f
        if f % 1 == 0:
            f = int(f)
    elif action == "**":
        f = s ** b
        if f % 1 == 0:
            f = int(f)
    else:
        return "error"
    return f

def ma(update, context):
    chat = update.effective_chat
    l = update.message.text
    l = l.replace(' ', '')
    f = 0
    g = 0
    for i in l:
        if i.isdigit():
            f += 1
        elif i == '.':
            f += 1
        else:
            d = f
            g += 1
    print(g)
    if g == 1:
        v = float(l[0 : d])
        n = float(l[d+1 : len(l)])
        c = l[d]
    elif g == 2:
        v = float(l[0: d - 1])
        n = float(l[d + 1: len(l)])
        c = l[d-1:d]
    print(v)
    print(n)
    print(c)
    g = ca(v, n, c)
    if g % 1 < 0.000001:
        g = g // 1
        g = int(g)
    context.bot.send_message(chat_id=chat.id, text=g)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ma))
updater.start_polling()
updater.idle()
