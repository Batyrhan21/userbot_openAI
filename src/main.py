from decouple import config
from pyrogram import Client, filters

from service import OpenAIService


api_id = config('API_ID')
api_hash = config('API_HASH')

app = Client('my_account', api_id=api_id, api_hash=api_hash)

ADMIN=927747990

@app.on_message(filters.text & filters.private & ~filters.user(ADMIN))
async def openai(client, message):
    await message.reply_text(OpenAIService.openai_response(message.text))

app.run()