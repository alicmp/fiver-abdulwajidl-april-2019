import os

from telethon.sync import TelegramClient

api_id = os.environ('API_ID')
api_hash = os.environ('API_HASH')
phone = os.environ('PHONE_NUMBER')
client = TelegramClient(phone, api_id, api_hash)

def login():
    client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter the code: '))


from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
