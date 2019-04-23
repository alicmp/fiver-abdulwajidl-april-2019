# Telegram Scraper
With this project you can scrape data from certain telegram channels and post these data to your facebook page.
## Requirements
- Python 3.6
- pipenv
## Configuration
First Create .env file and put these info in it:
```
API_ID =
API_HASH = ""
PHONE_NUMBER = ""

FB_ACCESS_TOKEN = ""

FB_APP_ID = 
FB_APP_SECRET = ""
```
Then create virtual environment by typing
`pipenv shell`
Then install packages
`pipenv install`
Finally run the code
`python main.py`