API_BASE_URL = 'http://127.0.0.1:8000'

ADMIN_USER = '@REPLACE WITH YOUR Telegram USERNAME'
BOT_TOKEN = 'REPLACE WITH YOUR TOKEN'

TEXT_WELCOME = """Welcome to the WebAPI Bot!

Make sure you have your backend API up and running.

Here is the list of available commands:
/start - show this welcome screen
/show - get variable number of items in given category (default = all)
/create - to create new item, e.g. '/create products title=IPhone price_rub=10'
/update - to change item info, e.g. '/update products 1 price_rub=999'
/delete - to remove item, e.g. '/delete products 1'

Note that only bot admin is allowed to run /create, /update and /delete commands. """
