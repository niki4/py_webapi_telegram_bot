Backend for Telegram bot that can run CRUD operations on your Web API (REST).

It has built-in abilities to restrict performing _unsafe_ operations
(POST/PUT/DELETE methods) only to bot admin, allowing GET for all users.
Additionally it supports
Web API that requires authentication.

Sounds interesting? Give a try it with the following Web API's:
* [py_webapi_django_example](https://github.com/niki4/py_webapi_django_example) - without authentication.
* [py_webapi_django_elearning_example](https://github.com/niki4/py_webapi_django_elearning_example) - with authentication.

## Installation:
First of all, using your command line clone the repo with bot backend, then create and activate
virtual environment:
```bash
git clone https://github.com/niki4/py_webapi_telegram_bot
cd py_webapi_telegram_bot

python3 -m venv ./venv
source venv/bin/activate
```
Install all dependencies with pip:
```bash
pip install -r requirements.txt
```

Now login to your regular Telegram client and open chat with [@BotFather](https://t.me/BotFather).
This is a bot that helps to register and manage another bots.
Thus, register a new bot sending following command to BotFather:
```
/newbot
```
Once your bot registered in Telegram, BotFather will provide you a token
to access the HTTP API. Copy it.

Now it's time to set up some settings. Open `settings.py` and paste
previously copied Telegram API token as value for `BOT_TOKEN`.
Yet replace `ADMIN_USER` with your own Telegram username
(keep the @ symbol at the beginning).

If you choosed to run the bot with Web API _without_ authentication
(like [py_webapi_django_example](https://github.com/niki4/py_webapi_django_example)),
you're all set. Make sure you have the Web API set up and running,
then go on to Run section.

But if your Web API requires authentication, e.g.
[py_webapi_django_elearning_example](https://github.com/niki4/py_webapi_django_elearning_example),
you additionally have to set credentials for that Web API in system variables.
For example:
```bash
export API_LOGIN=admin
export API_PASS=adminpassword
```
> For Windows users:
use __set__ instead of __export__ to create system variable from command line.

## Run:
Simply run bot.py script:
```bash
python bot.py
```
Now open conversation with your bot in Telegram client.

Send `/start` command to retrieve list of available actions:
```bash
Welcome to the WebAPI Bot!

Make sure you have your backend API up and running.

Here is the list of available commands:
/start - show this welcome screen
/show - get variable number of items in given category (default = all)
/create - to create new item, e.g. '/create products title=IPhone price_rub=10'
/update - to change item info, e.g. '/update products 1 price_rub=999'
/delete - to remove item, e.g. '/delete products 1'

Note that only bot admin is allowed to run /create, /update and /delete commands.
```

First param after command should always be desired Web API endpoint (category).
For example, if we have browsable Web API address http://127.0.0.1:8000/tags/
to list all the tags, we could send following command to our telegram bot
to get the same list:
```bash
/show tags
```

To get the info _only for particular item_, specify its id (pk) number
as a second param after command. Following is an equivalent to GET
request to Web API address http://127.0.0.1:8000/tags/3/:
```bash
/show tags 3
```

When creating (=POST) and updating (=PUT) data with bot, you can provide
arbitrary number of fields that item requires in '_key=value_' format
(note that there no spaces around equality sign!). For example:
```bash
/create webinars title=Python3 description=Advanced scheduled_time=2018-05-12T20:21:03Z
```
If success, bot will response with the following message:
```
Created.
{"id":2,"title":"Python3","description":"Advanced","scheduled_time":"2018-05-12T20:21:03Z"}
```
> Use __only spaces__ to separate params in commands for bot.

## Docs:
This project created with usage of
[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
framework and utilizes [Telegram Bot API](https://core.telegram.org/bots/api).

 Kindly check these projects docs to learn how it works if you're about
 to amend this example project on your own taste.