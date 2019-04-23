import os
import requests
# from requests_toolbelt import MultipartEncoder
from graphapiext import GraphAPIExt

access_token = os.environ.get('FB_ACCESS_TOKEN')
# access_token = 'EAAIghCwTMBwBAH0Ozt1bi1UZBtCIh8pbxZB9UW8qzTG56nd3XRYWAJJZCflZCN6vGhl4vFWbqzAF9RuYSoaZCnsr9dsU2RGKhHRUiJNNVJNsytglhj3wZBnKyxlJw5kZBVdip6EVOgtQaHQHQseNNgWpIe5GLpIZAA1NgCBzKBdSLQZDZD'
app_id = os.environ.get('FB_APP_ID')
app_secret = os.environ.get('FB_APP_SECRET')

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
