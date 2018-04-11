#! usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import traceback

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

driver = webdriver.Firefox()
driver.get('https://www.tripadvisor.com/Attraction_Review-g294201-d553185-Reviews-Keops_Pyramid-Cairo_Cairo_Governorate.html')
source = driver.page_source
soup = bs4.BeautifulSoup(source, "html.parser")
last = soup.select("a.pageNum.last.taLnk")
print(last[0].text)

pages = []

try:
    
    for page in range(int(last[0].text) - 1):

        # <div class="loadingWhiteBox">
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")))
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "next")))
        
##        reviews = driver.find_elements_by_class_name('review-container')
##        for review in reviews:
##            pages.append(review.text)

        page_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")
        page = page_obj.select("#taplc_location_reviews_list_responsive_detail_0")
        pages.append(page[0])
        # print(page[0].text.translate(non_bmp_map))
        
        driver.find_element_by_class_name('next').click()
        
except Exception as ex:
    print(traceback.format_exc())

finally:    
    driver.close()
    print(len(pages))

