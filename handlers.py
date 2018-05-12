import os
import requests

from settings import TEXT_WELCOME, API_BASE_URL


def start_bot_callback(bot, update):
    update.message.reply_text(TEXT_WELCOME)


def show_item_callback(bot, update, args=None):
    if len(args) > 1:
        items_info = requests.get('/'.join([API_BASE_URL, args[0], args[1]])).json()
    elif len(args) == 1:
        items_info = requests.get('/'.join([API_BASE_URL, args[0]])).json()
    else:
        items_info = 'Please, provide Category name as a first param and ' \
                     '(optionally) item ID number as a second.'
    update.message.reply_text(items_info)


def create_item_callback(bot, update, args=None):
    if len(args) >= 2:
        request_data = dict()
        for param in args[1:]:
            pair = param.split(sep='=')
            request_data[pair[0]] = pair[1]
        response = requests.post(
            url='/'.join([API_BASE_URL, args[0], '']),
            data=request_data,
            auth=(os.environ['API_LOGIN'], os.environ['API_PASS']) if all(
                ['API_LOGIN' in os.environ, 'API_PASS' in os.environ]) else None)
        update.message.reply_text('%s.\n%s' % (response.reason, response.text))
    else:
        update.message.reply_text('Please, provide Category name and set of Values that item requires.')


def update_item_callback(bot, update, args=None):
    if len(args) > 2:
        request_data = dict()
        for param in args[2:]:
            pair = param.split(sep='=')
            request_data[pair[0]] = pair[1]
        response = requests.put(
            url='/'.join([API_BASE_URL, args[0], args[1], '']),
            data=request_data,
            auth=(os.environ['API_LOGIN'], os.environ['API_PASS']) if all(
                ['API_LOGIN' in os.environ, 'API_PASS' in os.environ]) else None)
        update.message.reply_text('%s.\n%s' % (response.reason, response.text))
    else:
        update.message.reply_text('Please, provide Category name, item ID and set of Values to update.')


def delete_item_callback(bot, update, args=None):
    if len(args) == 2:
        response = requests.delete(
            url='/'.join([API_BASE_URL, *args]),
            auth=(os.environ['API_LOGIN'], os.environ['API_PASS']) if all(
                ['API_LOGIN' in os.environ, 'API_PASS' in os.environ]) else None)
        update.message.reply_text('%s.\n%s' % (response.reason, response.text))
    else:
        update.message.reply_text('Please, provide Category name and ID of item you want to delete.')


def unknown_command_callback(bot, update):
    update.message.reply_text("Sorry, the command is not supported or not allowed.")
