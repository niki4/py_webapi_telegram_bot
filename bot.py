import logging

from telegram.ext import CommandHandler, MessageHandler, Updater, Filters
from settings import ADMIN_USER, BOT_TOKEN
from handlers import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


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
