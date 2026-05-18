from pyrogram import Client, filters

# API details
API_ID = 12345678
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

# IDs
SOURCE_GROUP = -1002294325631   # Group ID
TARGET_CHANNEL = -1003775458189  # Channel ID

app = Client(
    "forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Only documents/files
@app.on_message(
    filters.chat(SOURCE_GROUP) &
    filters.document
)
async def forward_docs(client, message):
    try:
        await message.forward(TARGET_CHANNEL)
        print("Document forwarded")
    except Exception as e:
        print(e)

app.run()
