import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import json

def load_conversations(file_name):
    with open(file_name, 'r') as f:
        conversations = json.load(f)
    return conversations

def handle_message(bot, update, conversations):
    message = update.message.text.lower()
    if message in conversations:
        response = random.choice(conversations[message])
        update.message.reply_text(response)
    else:
        update.message.reply_text("I'm sorry, I don't understand.")

conversations = load_conversations('conversations.json')

bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN')
dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text, handle_message, pass_args = (conversations))
dispatcher.add_handler(message_handler)

updater.start_polling()
