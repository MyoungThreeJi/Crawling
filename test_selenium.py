from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "https://m.post.naver.com/viewer/postView.naver?volumeNo=31021151&memberNo=53003059&navigationType=push"

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)

### 스크래핑 부분 ###

# 제목(제조사, 제품명)
title = driver.find_element_by_class_name("se_textarea")
print(title.text)

# 테이블(성분명, 검출량, 부작용 정보)
table = driver.find_element_by_class_name("se_table_col")

for tr in table.find_elements_by_tag_name("tr"):
    td = tr.find_elements_by_tag_name("td")
    s = "{} , {} , {}".format(td[0].text, td[1].text, td[2].text)
    print(s)
