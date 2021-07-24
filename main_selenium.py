from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
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
for page in range(3,4): # TEST: 3페이지
    contentList = []
    driver.find_elements_by_class_name("spot_post_area")[page].click()
    # time.sleep(3)


### 스크래핑 부분 ###

    # 제목(제조사, 제품명)
    title = driver.find_element_by_class_name("se_textarea")
    print(title.text)
    # 제조사
    print(' '.join(title.text.split()[1:2]))
    # 제품명
    print(' '.join(title.text.split()[1:]))

    # 제품이미지
    image=driver.find_element_by_class_name("se_mediaImage.__se_img_el")
    print(image.get_attribute('src'))
    url = image.get_attribute('src')
    file_name=str(' '.join(title.text.split()[1:]))+'.jpg'
    urllib.request.urlretrieve(url, file_name)


    # 테이블(성분명, 검출량, 부작용 정보)
    table = driver.find_element_by_class_name("se_table_col")
    contentList.append(' '.join(title.text.split()[1:]))
    for tr in table.find_elements_by_tag_name("tr"):
        singleList = []
        try:
            td = tr.find_elements_by_tag_name("td")
            # s = "{} , {} , {}\n".format(td[0].text, td[1].text, td[2].text)
            # print(s)
            # singleList.append(image.get_attribute('src'))
            if str(td[0].text)=='성분명':
                continue
            name=str(td[0].text)
            KoName,EnName=name.split('\n')
            print(KoName,EnName)
            singleList.append(KoName)
            singleList.append(EnName)
            singleList.append(td[1].text)

            effect=str(td[2].text)
            effect=effect.replace('-','')
            list=effect.split('\n')
            singleList.append(list)
            print(singleList)
            contentList.append(singleList)
        except:
            break
    

    searchList.append(contentList)
    driver.back()

toCSV(searchList)
