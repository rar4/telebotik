from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json as d
import datetime
TOKEN = '5269119122:AAHUTCgZkvZ6Nwu01D6K4AI800HZ85Bz8CI'
print("Bot is bot")
updater = Updater(TOKEN)


def ah(update, context):
    chat = update.effective_chat
    mas = update.message.text
    context.bot.send_message(chat_id=chat.id, text=mas)
    lol(update)


def lol(update ):
    try:
        with open('sus.json', 'a') as g:
         g.close()
    except:
        with open('sus.json', 'w') as g:
         g.close()
    with open('sus.json', 'a') as g:
        a = datetime.datetime.now()
        sus =  {
            """inf""" : {
            "user" : {"user id" : update.message.chat.id, "user name" : update.message.chat.first_name},
            "message": {"text": update.message.text, "id": update.message.message_id},
            "date": a
        }}

        ss = str(f"""{sus}\n""")
        ss = ss.replace("'", '"')
        ss = ss.replace('datetime.datetime', '')
        ss = ss.replace('(', '[')
        ss = ss.replace(')', ']')
        print(ss)
        g.write(ss)


disp = updater.dispatcher
disp.add_handler(MessageHandler(Filters.all, ah))
updater.start_polling()
updater.idle()
