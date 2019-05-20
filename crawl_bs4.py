from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

print('네이버 실시간 검색어 순위') 

url = 'https://www.naver.com/'
print('url pulled')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
rank_items = soup.find_all(class_='div.ah_roll.PM_CL_realtimeKeyword_rolling_base')
item_array = []
print('item crawled')

for item in rank_items:
    item_array.append(item.get('pan.ah_k'))

count=0
for title in ranks:
    count += 1
    print(str(count) + '. ' + title.text)
    
driver.quit()