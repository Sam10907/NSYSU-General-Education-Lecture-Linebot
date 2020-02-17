# NSYSU-General-Education-Lecture-Linebot
中山大學大學之道的linebot，提供查詢大學之道的講座日期以及英文自學園的講座日期，並且在講座當天早上會自動提醒你今天有演講，避免因忘記而影響到畢業，由於現在學校還沒公佈下學期的大學之道演講日期，所以目前只會在每天早上9點跟你說早安，待正式日期公佈後我在進行修改。

這個專案的linebot是使用Line api with Python SDK製作而成，並且使用Django當linebot server，處理用戶傳來的訊息並給予適當的回覆。

Line api Python SDK -> https://github.com/line/line-bot-sdk-python#message

# heroku+GCP
由於heroku的免費dyno專案限制網站運作時間，不能24小時都保持清醒，至少必須休眠6小時（18+6），且原先也已經將專案部署到heroku，為了節省不必要的麻煩，於是透過在GCP服務裡新建一個ubuntu的虛擬機器，使用crontab(linux內建的排程工具)將req.py加入虛擬機的排程並在早上8點到晚上11點每個小時的45分執行此程式，呼叫我的heroku專案，這樣的方法可使得heroku有足夠的休眠時間，畢竟heroku在啟動後的30分鐘後將會自動休眠。
crontab的使用方法 -> http://linux.vbird.org/linux_basic/0430cron.php
GCP的創建與排程方法 -> https://jerrynest.io/gcp-server/    +    https://www.maxlist.xyz/2018/09/29/gcp_server_python/
