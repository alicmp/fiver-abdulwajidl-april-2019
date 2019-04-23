import os
import getpass

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon import events

import fb

import logging
logging.basicConfig(level=logging.ERROR)


def get_channels():
    channels = []
    with open('channels.txt', 'r') as f:
        channels = f.readlines()
    return tuple(channels)


api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')
client = TelegramClient(phone, api_id, api_hash)


print("start log in to telegram ...")


client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=getpass.getpass())


print("successful login")


@client.on(events.NewMessage(chats=get_channels()))
async def handler(event):
    print("start scraping data from telegram")
    media_path = None
    raw_text = event.raw_text
    if event.media:
        media_path = await client.download_media(event.media, file='media/')
    
    fb.send_msg(raw_text, media_path)


client.run_until_disconnected()
