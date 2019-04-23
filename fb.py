import os
import requests

from configparser import ConfigParser
from graphapiext import GraphAPIExt

import logging
logging.basicConfig(level=logging.ERROR)

cfg = ConfigParser()
cfg.read('config.ini')

access_token = cfg.get('facebook', 'FB_LONG_LIVE_ACCESS_TOKEN')
app_id = cfg.get('facebook', 'FB_APP_ID')
app_secret = cfg.get('facebook', 'FB_APP_SECRET')

fb = GraphAPIExt(
    access_token=access_token
)

def send_msg(text, media):
    if media and 'jpg' in media:
        fb.put_photo(
            image=open(media, 'rb'),
            message=text
        )
        print("send one message containing photo")
    elif media and 'mp4' in  media:
        fb.put_video(
            video=open(media, 'rb'),
            video_name=media.split('/')[-1],
            message=text
        )
        print("send one message containing video")
    else:
        fb.put_object(
            parent_object='me',
            connection_name='feed',
            message=text
        )
        print("send one message")



def get_long_live_token():
    access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(
        app_id, app_secret, access_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    user_long_token = access_token_info['access_token']

    print(access_token_info)
