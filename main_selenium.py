from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

def toCSV(data):
    df = pd.DataFrame(data)
    # df.columns = ["타이틀", "성분", "검출량", "부작용"] # 불규칙적인 행 개수
    df.to_csv("pad_data.csv", index=True, mode='w', header=False)


url="https://m.post.naver.com/my/series/detail.naver?seriesNo=640254&memberNo=53003059&prevVolumeNo=31021100"
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)

while True:
    try:
        plus = driver.find_element_by_css_selector("div.btn_paging_area")
        plus.click()
    except:
        break

searchList = []
for page in range(3,7): # TEST: 3페이지
    contentList = []
    driver.find_elements_by_class_name("spot_post_area")[page].click()
    # time.sleep(3)


### 스크래핑 부분 ###

    # 제목(제조사, 제품명)
    title = driver.find_element_by_class_name("se_textarea")
    print(title.text)

    # 제품이미지
    # image = driver.find_element_by_class_name("se_mediaImage __se_img_el")
    # print(image.get_attribute('src'))

    # 테이블(성분명, 검출량, 부작용 정보)
    table = driver.find_element_by_class_name("se_table_col")
    contentList.append(title.text)
    for tr in table.find_elements_by_tag_name("tr"):
        singleList = []
        try:
            td = tr.find_elements_by_tag_name("td")
            s = "{} , {} , {}\n".format(td[0].text, td[1].text, td[2].text)
            print(s)
            # singleList.append(image.get_attribute('src'))
            singleList.append(td[0].text) # 
            singleList.append(td[1].text)
            singleList.append(td[2].text)
            contentList.append(singleList)
        except:
            break
    

    searchList.append(contentList)
    driver.back()

toCSV(searchList)
