## 匯入模組(Library)
import requests  
from bs4 import BeautifulSoup

url = (
    'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001006000&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1')

dom = requests.get(url).text # 取得該網頁中的HTML的內容
soup = BeautifulSoup(dom, 'html.parser') # 使用HTML中的內容創建Beautifulsoup物件, 方便解析
jobs = soup.find_all('article', class_="b-block--top-bord job-list-item b-clearfix js-job-item") # 篩選出HTML中所有article元素且class等於"b-block--top-bord job-list-item b-clearfix js-job-item", 並回傳為list


for job in jobs: # Go through上述得到的list, job會從jobs[0]一路走到jobs[len(jobs)-1]
    print(job.find('a',class_="js-job-link").text) # 職缺的名稱, job中尋找'a' tag的元素, 且class等於"js-job-link中的所有文字(包括子元素)
    print(job.get('data-cust-name')) #公司名稱, 取得"data-cust-name"屬性的內容
    print(job.find('p').text) #工作描述, job中"p"元素中的文字(包括子元素)
    print("----------------------------------------")

""" 尋找特定公司的職缺
for job in jobs:
    if (job.get('data-cust-name') == "聯詠科技股份有限公司") :
        print(job.find('a',class_="js-job-link").text)
        print(job.find('p').text)
"""