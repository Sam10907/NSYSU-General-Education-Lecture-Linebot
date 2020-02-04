from apscheduler.schedulers.blocking import BlockingScheduler
from linebot import LineBotApi
from django.conf import settings
import requests
import time

line_bot_api=LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
sched=BlockingScheduler()
sched.add_job(auto_broadcast,'interval',minutes=2, start_date='2020-2-4 23:55:00')
@sched.scheduled_job('interval', id='auto_id', minutes=2)
def auto_broadcast():
    line_bot_api.broadcast(TextSendMessage(text='今天沒有大學之道'))
    url='https://mychatbotproject.herokuapp.com/'
    requests.get(url)

sched.start()