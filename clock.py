from apscheduler.schedulers.blocking import BlockingScheduler
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import time

CHANNEL_ACCESS_TOKEN = "---------------------------"
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)
def auto_broadcast():
    line_bot_api.broadcast(TextSendMessage(text='同學早安阿!'))
def request(): #request heroku per 25 minutes so as not to sleep
    url='https://mychatbotproject.herokuapp.com/'
    requests.get(url)

sched=BlockingScheduler()
sched.add_job(auto_broadcast,'interval',days=1, start_date='2020-2-5 01:00:00')
sched.add_job(request,'interval',minutes=25)
sched.start()
