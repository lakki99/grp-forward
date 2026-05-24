import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("30645970"))
API_HASH = os.environ.get("2c48e706842683ac68160cdd0d5560f8")
BOT_TOKEN = os.environ.get("8793396352:AAFrMNoAHteI7uoH52oF9T6-pHaFqTaVI5s")

SOURCE_GROUP = int(os.environ.get("-1002294325631"))
TARGET_CHANNEL = int(os.environ.get("-1003775458189"))

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.chat(SOURCE_GROUP) & filters.document)
async def forward(client, message):
    await message.forward(TARGET_CHANNEL)

app.run()
