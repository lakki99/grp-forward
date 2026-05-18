import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

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
