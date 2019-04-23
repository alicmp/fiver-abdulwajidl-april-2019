# Telegram Scraper
With this project you can scrape data from certain telegram channels and post these data to your facebook page.
## Requirements
- Python 3.6
- pipenv
- celery
- RabbitMQ
## Configuration
First Create congig.ini file and put these info in it:
```
API_ID =
API_HASH = ""
PHONE_NUMBER = ""

FB_ACCESS_TOKEN = ""

FB_APP_ID = 
FB_APP_SECRET = ""
```
Then create virtual environment by typing
```
pipenv shell
```
Then install packages
```
pipenv install
```
You have to install RabbitMQ, you can install it on linux like this:
```
sudo apt-get install rabbitmq-server
sudo service rabbitmq-server restart
```
We have to keep in mind if we send too many posts in short period of time facebook ban us. So we should send each post periodically. To achieve this goal i use celery and rabbitMQ. By running below command, queued tasks run synchronosly and serially.
```
celery -A fb worker --concurrency=1 --loglevel=info
```
Finally open another termianl and run:
```
python main.py
```