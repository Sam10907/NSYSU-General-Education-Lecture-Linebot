from apscheduler.schedulers.blocking import BlockingScheduler
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import time

CHANNEL_ACCESS_TOKEN = "Ps1DeC+Mswm2Zpd14q3sa/3/I1g5+MiiqiHD8mqPNa8ykCuQ7wJ+tIuJE6qVdf6uNNGge1Fzk+nwmZAc8s/LyMcEQK7wwSKEBIHQCLEo00YyRiwgE1FT8I28s2pc2Qs+mNVMNzBC316oal2zyMhfdgdB04t89/1O/w1cDnyilFU="
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)
def auto_broadcast():
    line_bot_api.broadcast(TextSendMessage(text='同學早安阿!'))
def request():
    url='https://mychatbotproject.herokuapp.com/'
    requests.get(url)

sched=BlockingScheduler()
sched.add_job(auto_broadcast,'interval',days=1, start_date='2020-2-5 01:00:00')
sched.add_job(request,'interval',minutes=25)
sched.start()