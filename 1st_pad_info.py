from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import time

def toCSV(data):
    df = pd.DataFrame(data)
    df.columns = ["pad_id", "manufacturer", "name", "image"]
    df.to_csv("pad_info.csv",index=False, mode='w', header=True)


url="https://m.post.naver.com/my/series/detail.naver?seriesNo=640254&memberNo=53003059&prevVolumeNo=31021100"
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)

while True:
    try:
        plus = driver.find_element_by_css_selector("div.btn_paging_area")
        plus.click()
        time.sleep(1)
    except:
        break

searchList = []
id = 1
pages = len(driver.find_elements_by_class_name("spot_post_area"))
for page in range(3,pages):
    try:
        singleRow = []
        driver.find_elements_by_class_name("spot_post_area")[page].click()


    ### 스크래핑 부분 ###

        # 제목(제조사, 제품명)
        title = driver.find_element_by_class_name("se_textarea")
        # 제조사
        manufacturer = ' '.join(title.text.split()[1:2])
        # 제품명
        name = ' '.join(title.text.split()[1:])

        # 제품이미지
        image=driver.find_element_by_class_name("se_mediaImage.__se_img_el").get_attribute('src')
        # file_name=str(' '.join(title.text.split()[1:]))+'.jpg'
        # urllib.request.urlretrieve(image, file_name)

        singleRow.append(id)
        singleRow.append(manufacturer)
        singleRow.append(name)
        singleRow.append(image)
        searchList.append(singleRow)

        id = id + 1
        driver.back()
    
    except:
        driver.back()
        continue

toCSV(searchList)
