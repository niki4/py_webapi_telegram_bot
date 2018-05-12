import logging
import requests

from telegram.ext import CommandHandler, MessageHandler, Updater, Filters

API_BASE_URL = 'http://127.0.0.1:8000'
ADMIN_USER = '@REPLACE WITH YOUR USERNAME'
BOT_TOKEN = 'REPLACE WITH YOUR TOKEN'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def start_bot_callback(bot, update):
    text_welcome = """Welcome to the WebAPI Bot!

Make sure you have your backend API up and running.

Here is the list of available commands:
/start - show this welcome screen
/show - get variable number of items in given category (default = all)
/create - to create new item, e.g. '/create products title=IPhone price_rub=10'
/update - to change item info, e.g. '/update products 1 price_rub=999'
/delete - to remove item, e.g. '/delete products 1'

Note that only bot admin is allowed to run /create, /update and /delete commands. """
    update.message.reply_text(text_welcome)


def show_item_callback(bot, update, args=None):
    if len(args) > 1:
        items_info = requests.get('/'.join([API_BASE_URL, args[0], args[1]])).json()
    elif len(args) == 1:
        items_info = requests.get('/'.join([API_BASE_URL, args[0]])).json()
    else:
        items_info = 'Please, provide category name as a first param and' \
                     ' (optionally) item id number as a second.'
    update.message.reply_text(items_info)


def create_item_callback(bot, update, args=None):
    if len(args) >= 2:
        request_data = dict()
        for param in args[1:]:
            pair = param.split(sep='=')
            request_data[pair[0]] = pair[1]
        response = requests.post('/'.join([API_BASE_URL, args[0], '']), data=request_data)
        update.message.reply_text(response.reason)
    else:
        update.message.reply_text('Please, provide Category name and set of Values that item requires.')


def update_item_callback(bot, update, args=None):
    if len(args) > 2:
        request_data = dict()
        for param in args[2:]:
            pair = param.split(sep='=')
            request_data[pair[0]] = pair[1]
        response = requests.put('/'.join([API_BASE_URL, args[0], args[1], '']), data=request_data)
        update.message.reply_text(response.reason)
    else:
        update.message.reply_text('Please, provide Category name, item ID and set of Values to update.')


def delete_item_callback(bot, update, args=None):
    if len(args) == 2:
        response = requests.delete('/'.join([API_BASE_URL, *args]))
        update.message.reply_text(response.reason)
    else:
        update.message.reply_text('Please, provide Category name and ID of item you want to delete.')


def unknown_command_callback(bot, update):
    update.message.reply_text("Sorry, the command is not supported or not allowed.")


def main():
    updater = Updater(token=BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler(
        'start', start_bot_callback))
    dp.add_handler(CommandHandler(
        'show', show_item_callback, pass_args=True))
    dp.add_handler(CommandHandler(
        'create', create_item_callback, pass_args=True, filters=Filters.user(username=ADMIN_USER)))
    dp.add_handler(CommandHandler(
        'update', update_item_callback, pass_args=True, filters=Filters.user(username=ADMIN_USER)))
    dp.add_handler(CommandHandler(
        'delete', delete_item_callback, pass_args=True, filters=Filters.user(username=ADMIN_USER)))
    dp.add_handler(MessageHandler(Filters.command, unknown_command_callback))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
