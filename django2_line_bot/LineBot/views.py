import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, StickerMessage, StickerSendMessage
from .models import User_data
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger("django")

line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.CHANNEL_SECRET)

Message="歡迎來到中山大學之道，本官方帳號會自動在當日提醒您今天有大學之道的演講或者是英文自學園的講座，避免您錯過而影響畢業門檻，如要查詢大學之道或英文自學園的講座日期，請在訊息欄輸入「大學之道」或「英文自學園」我們將為您提供資訊。"

Text_list=['嗨~今天過的好嗎?','摳憐納','好棒喔~加油']

@csrf_exempt
@require_POST
def webhook(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = (
            "Invalid signature. Please check your channel access token/channel secret."
        )
        logger.error(messages)
        return HttpResponseBadRequest(messages)
    return HttpResponse("OK")
@handler.add(FollowEvent)
def followed(event:FollowEvent):
    if event.source.user_id != 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        User_data.objects.create(user_id=event.source.user_id)
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text=Message))
@handler.add(MessageEvent,message=TextMessage)
def send_information(event:MessageEvent):
    if event.source.user_id != 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        if '大學之道' in event.message.text:
            url='https://siwan.nsysu.edu.tw/wp-content/uploads/2020/03/%E3%80%8C%E5%A4%A7%E5%AD%B8%E4%B9%8B%E9%81%93%EF%BC%9A%E4%B8%AD%E5%B1%B1%E9%80%9A%E8%AD%98%E6%95%99%E8%82%B2%E8%AC%9B%E5%BA%A7%E3%80%8D108%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC2%E5%AD%B8%E6%9C%9F%E6%B4%BB%E5%8B%95%E5%BD%99%E6%95%B4%E8%A1%A8-109.3.5.pdf'
            message_list=[TextMessage(text=url),StickerMessage(package_id='11537',sticker_id='52002763')]
            line_bot_api.reply_message(event.reply_token,message_list)
        elif '英文自學園' in event.message.text:
            url1='http://zephyr.nsysu.edu.tw:8080/'
            message_list1=[TextMessage(text=url1),StickerMessage(package_id='11538',sticker_id='51626496')]
            line_bot_api.reply_message(event.reply_token,message_list1)
        else:
            message_list2=[TextMessage(text='目前沒有此服務'),StickerMessage(package_id='11538',sticker_id='51626529')]
            line_bot_api.reply_message(event.reply_token,message_list2)
@handler.add(MessageEvent,message=StickerMessage)
def send_sticker(event:MessageEvent):
    if event.source.user_id != 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(event.message.package_id,event.message.sticker_id))
@handler.add(MessageEvent)
def send_text(event:MessageEvent):
    if event.source.user_id != 'Udeadbeefdeadbeefdeadbeefdeadbeef':
        try:
            user=User_data.objects.get(user_id=event.source.user_id)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=Text_list[user.text_index]))
            user.text_index+=1
            if user.text_index > 2:
                user.text_index=0
            user.save()
        except ObjectDoesNotExist:
            user=User_data.objects.create(user_id=event.source.user_id)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=Text_list[user.text_index]))
            user.text_index+=1
            user.save()
