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
        app.send_message(message.chat.id,f"Status set: **{status}**")
    except AboutTooLong:
        app.send_message(message.chat.id, f"The **{status}** status is too long. Try to shorten it")

@app.on_message(filters.command("remove_status", prefixes='!') & filters.me)
def status(client_object, message: types.Message):
    bio = app.get_chat(message.from_user.id).bio
    if "TgStatus" in bio:
        bio = str(bio).replace(f" |{str(bio).split('|')[-1]}", "")
        app.update_profile(bio=bio)
        app.send_message(message.chat.id, "Status removed")
    else:
        app.send_message(message.chat.id, "You have no status")

app.run()