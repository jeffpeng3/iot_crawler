## 匯入模組(Library)
import requests  
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Stock/index.html"
dom = requests.get(url).text # 取得該網頁中的HTML的內容
soup = BeautifulSoup(dom, 'html.parser') # 使用HTML中的內容創建Beautifulsoup物件, 方便解析
post = soup.select("#main-container > div.r-list-container.action-bar-margin.bbs-screen > div[class=r-ent] > div[class=title] > a") # 篩選出HTML中所有article元素且class等於"b-block--top-bord job-list-item b-clearfix js-job-item", 並回傳為list


for i in post:
    print(i.decode_contents(),"\n")