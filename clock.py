from apscheduler.schedulers.blocking import BlockingScheduler
from linebot import LineBotApi
from linebot.models import TextMessage,StickerMessage
import time
from datetime import date

CHANNEL_ACCESS_TOKEN = "..............."
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)
lecture_date=['2020-03-11','2020-05-08','2020-05-22']
lecture_time_location=['19:00-20:30在國研大樓1F階梯教室','14:00-16:00在國研大樓光中廳','13:30-16:00在演藝廳']
lecture_topic=['音樂會 競技<大協奏曲>','2020 周大觀熱愛生命分享活動','宅宅鄉民創業路！「電獺少女」創辦人不呱張開講']

def auto_broadcast():
    message='提醒您 今天'+lecture_time_location[0]+'有講座 '+lecture_topic[0]+'，不要錯過了！！'
    if date.today().isoformat() == lecture_date[0]:
        messages_list=[TextMessage(text=message),StickerMessage(package_id='11537',sticker_id='52002738')]
        line_bot_api.broadcast(messages_list)
        lecture_date.remove(lecture_date[0])
        lecture_time_location.remove(lecture_time_location[0])
        lecture_topic.remove(lecture_topic[0])

sched=BlockingScheduler()
sched.add_job(auto_broadcast,'interval',days=1, start_date='2020-3-11 01:00:00')
sched.start()
