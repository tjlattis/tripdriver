#! usr/local/bin/python3
# tripindex.py | a script which will scrape links to 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import tripdriver

driver = webdriver.Firefox()
url = "https://www.tripadvisor.com/Attractions-g294201-Activities-c47-Cairo_Cairo_Governorate.html#FILTERED_LIST"
driver.get(url)

for i in range(4):

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")))

    page_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")
    listings = page_obj.select(".listing_title")
    
    for listing in listings:

        link = listing.find('a')
        linkurl = "https://www.tripadvisor.com" + link.get('href')
        tripdriver.GetComments(linkurl)

    driver.find_element_by_class_name('next').click()


driver.close()
    
