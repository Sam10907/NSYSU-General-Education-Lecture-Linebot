# NSYSU-General-Education-Lecture-Linebot
中山大學大學之道的linebot，提供查詢大學之道的講座日期以及英文自學園的講座日期，並且在講座當天早上會自動提醒你今天有演講，避免因忘記而影響到畢業，由於現在學校還沒公佈下學期的大學之道演講日期，所以目前只會在每天早上9點跟你說早安，待正式日期公佈後我在進行修改。

這個專案的linebot是使用Line api with Python SDK製作而成，並且使用Django當linebot server，處理用戶傳來的訊息並給予適當的回覆。

Line api Python SDK -> https://github.com/line/line-bot-sdk-python#message

# heroku restart problem
由於heroku每隔24小時+random minute會強制休眠，所以有時候早上會收不到訊息，記得定時傳訊息給linebot，以便喚醒linebot的heroku後台程序。
