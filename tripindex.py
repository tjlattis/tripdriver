#! usr/local/bin/python3
# tripindex.py | a script which will scrape links to POIs in a given city on tripadvisor when provided the proper url
# calls annother instance of the webdriver which scrapes the comments from the pages indexed by this script

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import tripdriver
from datetime import datetime

def ScrapeIndex(url):
	driver = webdriver.Firefox()
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

if __name__ == "__main__":

	start_time = datetime.now()
	url = "https://www.tripadvisor.com/Attractions-g294201-Activities-c47-Cairo_Cairo_Governorate.html#FILTERED_LIST"
	ScrapeIndex(url)
	print("Job Completed!")
	print("time elapsed : %s" % (datetime.now() - start_time)) 
    
