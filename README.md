# NSYSU-General-Education-Lecture-Linebot
中山大學大學之道的linebot，提供查詢大學之道的講座日期以及英文自學園的講座日期，並且在講座當天早上會自動提醒你今天有演講，避免因忘記而影響到畢業，由於現在學校還沒公佈下學期的大學之道演講日期，所以目前只會在每天早上9點跟你說早安，待正式日期公佈後我在進行修改。

這個專案的linebot是使用Line api with Python SDK製作而成，並且使用Django當linebot server，處理用戶傳來的訊息並給予適當的回覆。

Line api Python SDK -> https://github.com/line/line-bot-sdk-python#message

由於我是使用Line的免費專案，每個月最多只能由bot發500則訊息，如果收不到訊息可能就是這個月的額度用完了，煩請大家盡可能不要一直傳訊息給機器人消耗本月的訊息額度，敬請見諒~
