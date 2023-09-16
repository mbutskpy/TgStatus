from pyrogram import Client, filters, types
from configparser import ConfigParser
from time import sleep
from pyrogram.errors import AboutTooLong

# config init
config = ConfigParser()

config.read('config.ini')
api_id = config.get('pyrogram', 'api_id')
api_hash = config.get('pyrogram', 'api_hash')

# print("bot is start")

app = Client('my_account', api_id, api_hash)
@app.on_message(filters.command("status", prefixes='!') & filters.me)
def status(client_object, message: types.Message):
    status = message.text.replace("!status ", "")
    try:
        bio = app.get_chat(message.from_user.id).bio
        if "TgStatus" in bio:
            bio = str(bio).replace(f" |{str(bio).split('|')[-1]}", "")

        new_bio = f"{bio} | TgStatus: {status}"
        app.update_profile(bio=new_bio)
        app.send_message(message.chat.id,f"Установлен статус: **{status}**")
    except AboutTooLong:
        app.send_message(message.chat.id, f"Статус **{status}** слишком длинный. Попробуйте сократить его")

@app.on_message(filters.command("shaylushay", prefixes='!'))
def shaylushay(client_object, message: types.Message):
    app.send_message(message.chat.id, "We live")
    sleep(1)
    app.send_message(message.chat.id, "We love")
    sleep(1)
    app.send_message(message.chat.id, "We lie")
    sleep(1)
    app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKTpZlBLxH27F_WvLo6q0BOGl9RsX91gACLj8AAsf1IEiR1sZVvj_zZjAE")
    app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKTpZlBLxH27F_WvLo6q0BOGl9RsX91gACLj8AAsf1IEiR1sZVvj_zZjAE")
    app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKTpZlBLxH27F_WvLo6q0BOGl9RsX91gACLj8AAsf1IEiR1sZVvj_zZjAE")

@app.on_message(filters.command("remove_status", prefixes='!') & filters.me)
def status(client_object, message: types.Message):
    bio = app.get_chat(message.from_user.id).bio
    if "TgStatus" in bio:
        bio = str(bio).replace(f" |{str(bio).split('|')[-1]}", "")
        app.update_profile(bio=bio)
        app.send_message(message.chat.id, "Статус удален")
    else:
        app.send_message(message.chat.id, "У Вас нет статуса")

app.run()