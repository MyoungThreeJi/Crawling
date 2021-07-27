from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import time

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
        time.sleep(1)
    except:
        break

searchList = []
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
        file_name=str(' '.join(title.text.split()[1:]))+'.jpg'
        urllib.request.urlretrieve(image, file_name)

        # print(manufacturer, name, image)


        # 테이블(성분명, 검출량, 부작용 정보)
        table = driver.find_element_by_class_name("se_table_col")
        singleRow.append(manufacturer)
        singleRow.append(name)
        singleRow.append(image)
        for tr in table.find_elements_by_tag_name("tr"):
            ingredientList = []
            try:
                td = tr.find_elements_by_tag_name("td")
                if str(td[0].text)=='성분명':
                    continue
                KoName,EnName=str(td[0].text).split('\n')
                mg = td[1].text
                effect=str(td[2].text).replace('-','').split('\n')

                ingredientList.append(KoName)
                ingredientList.append(EnName)
                ingredientList.append(mg)
                ingredientList.append(effect)
                # print(ingredientList)

                singleRow.append(ingredientList)

            except:
                break

        searchList.append(singleRow)
        driver.back()
    
    except:
        driver.back()
        continue

toCSV(searchList)
