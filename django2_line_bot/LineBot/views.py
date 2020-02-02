import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent

logger = logging.getLogger("django")

line_bot_api = LineBotApi('Ps1DeC+Mswm2Zpd14q3sa/3/I1g5+MiiqiHD8mqPNa8ykCuQ7wJ+tIuJE6qVdf6uNNGge1Fzk+nwmZAc8s/LyMcEQK7wwSKEBIHQCLEo00YyRiwgE1FT8I28s2pc2Qs+mNVMNzBC316oal2zyMhfdgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3882dd8561c35fbbe0d9b4f53912da7b')

message="歡迎來到中山大學之道，本官方帳號會自動在當日提醒您今天有大學之道的演講或者是英文自學園的講座，避免您錯過而影響畢業門檻，如要查詢大學之道或英文自學園的講座日期，請在訊息欄輸入「大學之道」或「英文自學園」我們將為您提供資訊。"

@csrf_exempt
@require_POST
def webhook(request):
    signature = request.headers["X-Line-Signature"]
    body = request.body.decode()
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
        line_bot_api.broadcast(TextSendMessage(text=message))