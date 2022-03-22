from telegram.ext import *
import json as d
import datetime
TOKEN = '5269119122:AAHUTCgZkvZ6Nwu01D6K4AI800HZ85Bz8CI'
print("Bot is bot")
updater = Updater(TOKEN)


def wel(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Hello! I am your echo bot')


def echo(update, context):
    chat = update.effective_chat
    mas = update.message.text
    context.bot.send_message(chat_id=chat.id, text=mas)
    create_json(update)


def js_write(js):
    with open('sus.json', 'a') as f:
        d.dump(js, f, ensure_ascii=False)
        f.write('\n')


def dat():
    a = str(datetime.datetime.now())
    a = a.replace('datetime.datetime', '')
    ss = a.replace('(', '[')
    ss = ss.replace(')', ']')
    return ss

def create_json(update):
    print(update.message.chat.first_name)
    js_obj = {
        "user": {"chat id": update.message.chat.id, "user name" : update.message.chat.first_name},
        "message": {"text": update.message.text, "id": update.message.message_id},
        "date": dat()
    }
    js_write(js_obj)


disp = updater.dispatcher
disp.add_handler(CommandHandler('start', wel))
disp.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()

