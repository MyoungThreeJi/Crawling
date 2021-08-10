from numpy import sin, single
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

def toCSV(data):
    df = pd.DataFrame(data)
    df.columns = ["ingredient_id", "name", "average", "max", "min"] # 불규칙적인 행 개수
    df.to_csv("ingredient_info.csv", index=False, mode='w', header=True)


url="https://m.post.naver.com/viewer/postView.naver?volumeNo=31444426&memberNo=53003059&navigationType=push"
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)

searchList = []
id = 1
table = driver.find_element_by_class_name("se_table_col")
print(table)
for tr in table.find_elements_by_tag_name("tr"):
    singleRow = []
    try:
        td = tr.find_elements_by_tag_name("td")
        if str(td[0].text)=='성분명':
            continue
        name = td[0].text
        if (name.find('-')): #  != -1
            name = name.split('-')[-1]
        avg = td[1].text
        max = td[2].text
        min = td[3].text
        singleRow.append(id)
        singleRow.append(name)
        singleRow.append(avg)
        singleRow.append(max)
        singleRow.append(min)
        searchList.append(singleRow)
        id = id + 1

        singleRow = []
        name2 = td[4].text
        if (name2.find('-')):
            name2 = name2.split('-')[-1]
        avg2 = td[5].text
        max2 = td[6].text
        min2 = td[7].text
        singleRow.append(id)
        singleRow.append(name2)
        singleRow.append(avg2)
        singleRow.append(max2)
        singleRow.append(min2)        

        searchList.append(singleRow)
        id = id + 1

    except:
        break

toCSV(searchList)
