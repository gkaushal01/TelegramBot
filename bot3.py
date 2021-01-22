import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext
 #Enable logging
from telegram import Update,Bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 	                level=logging.INFO)
logger=logging.getLogger(__name__)
 
TOKEN ="1559775310:AAEaSRixz6mXPC74kNeHe2hiAe7jum7MOIg"
def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id , sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error("Update '%s' has caused error '%s", update, update.error)

def greeting(update: Update,context: CallbackContext):
    first_name = update.to_dict()['message']['chat']['first_name']
    update.message.reply_text("hi {}".format(first_name))

def message_handler(update: Update,context: CallbackContext):
    text = update.to_dict()['message']['text']
    update.message.reply_text(text)

def main():
    updater=Updater(TOKEN)
    dp=updater.dispatcher 

    
    dp.add_handler(CommandHandler("start" , greeting))
    dp.add_handler(CommandHandler("help" , help))
    
    dp.add_handler(MessageHandler(Filters.text , message_handler))
    dp.add_handler(MessageHandler(Filters.sticker ,echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info("Started polling...")
    updater.idle()

if __name__=="__main__":
    main()
