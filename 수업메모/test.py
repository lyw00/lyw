from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/samsung/Downloads/chromedriver')
driver.get('https://cafe.naver.com/joonggonara?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.menuid=1900%26search.boardtype=L')
bb2 = []
dataset = []
time.sleep(2)

driver.switch_to.frame("cafe_main")
for l in range(1,71):
    tag = driver.find_elements_by_xpath('//div[@class="article-board m-tcol-c"]//table/tbody/tr')
    bb2 = tag
    time.sleep(2)
    
    for i in range(len(bb2)):
        dataset.append(bb2[i].text)

    if l % 10 == 0:
        c10 = driver.find_element_by_link_text('다음')
        c10.click()
    else:
        a = str(l+1)
        c = driver.find_element_by_link_text(a)
        c.click()
    time.sleep(2)

driver.quit()