#! usr/local/bin/python3
# tripdriver.py | a script which will scrape comments from a given page on tripadvisor
# simply change the harcoded url to the desired target url and run
# tripdriver.py will create two files, a .txt file with comment text and a .html file with the source markup for each comment container scraped

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import traceback

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# establish driver and perform initial query
driver = webdriver.Firefox()
url = "https://www.tripadvisor.com/Attraction_Review-g294201-d553185-Reviews-Keops_Pyramid-Cairo_Cairo_Governorate.html"
driver.get(url)

# find max page index
source = driver.page_source
soup = bs4.BeautifulSoup(source, "html.parser")
last = soup.select("a.pageNum.last.taLnk")
# print(last[0].text) # uncomment this line for debugging index finder

# initialize list
pages = []

# these statements may eventually be unnested from try/except
try:
    
    # iterate throuhg indexes
    for page in range(int(last[0].text) - 1):

        # wait for 'next' element to be visible after ajax request
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")))
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "next"))) # this line left for historical purposes

        # grab container and append to list
        page_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")
        page = page_obj.select("#taplc_location_reviews_list_responsive_detail_0")
        pages.append(page[0])
        # print(page[0].text.translate(non_bmp_map)) # uncomment this line if emojis are causing print problems
        
        # advance page
        driver.find_element_by_class_name('next').click()
        
except Exception as ex:
    print(traceback.format_exc())

finally:
    # close the browser and print minor confirmation
    driver.close()
    print(len(pages))

# create a (somewhat)unique filename from url
filename = url[28:]

# write results to a file
with open("%s.html" % filename, 'w') as htmlfile:
    for item in pages:
        htmlfile.write(str(item))
    htmlfile.close()

with open("%s.txt" % filename, 'w') as txtfile:
    for item in pages:
        txtfile.write(item.text)
    txtfile.close()
