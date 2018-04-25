#! usr/local/bin/python3
# tripdriver.py | a script which will scrape comments from a given page on tripadvisor
# simply change the harcoded url to the desired target url and run
# tripdriver.py will create two files, a .txt file with comment text and a .html file with the source markup for each comment container scraped

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time
import bs4
import sys
import writePyxl

def logError(filename, count, last):
    with open("%s.log" % filename, 'w') as logfile:
        logfile.write("Problem incrementing page for attraction:")
        logfile.write(filename)
        logfile.write("\n")
        logfile.write("Pages harvested successfully: %s of %s" %(count, last))
        logfile.close()

def checkExists(driver, className):
    try:
        driver.find_element_by_class_name(str(className))
    except:
        return False

    return True

def GetComments(url):

    # instantiate some things
    driver = webdriver.Firefox()
    driver.get(url)
    pages = []
    filename = url[62:-5]
    if filename[0] == "-":
        filename = filename[1:]     
    count = 1
    print("Harvesting comments from site: %s" % filename)

    # find max page index
    source = driver.page_source
    soup = bs4.BeautifulSoup(source, "html.parser")
    index = soup.select("a.pageNum.last.taLnk")

    if len(index) == 0:
        last = 1
    else:
        last = index[0].text 
    
    if last == 1:

        # grab container and append to list
        page_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")
        page = page_obj.select("#taplc_location_reviews_list_responsive_detail_0")
        pages.append(page[0])
        # print(page[0].text.translate(non_bmp_map)) # uncomment this line if emojis are causing print problems

        print("Page %s of %s complete" % (count, last))
        count += 1

    else: 
        
        # iterate throuhg indexes
        for i in range(int(last)):

            # wait for 'next' element to be visible after ajax request
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")))
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "next"))) # this line left for historical purposes

            if checkExists(driver, 'close.ui_icon.times'):
                try:
                    time.sleep(2)
                    driver.find_element_by_class_name('close.ui_icon.times').click()
                    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "ulBlueLinks")))
                except:
                    print('could not close green bar')


            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "ulBlueLinks")))
                driver.find_element_by_class_name('taLnk.ulBlueLinks').click()
            except:
                try:
                    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "ulBlueLinks")))
                    driver.find_element_by_class_name('taLnk.ulBlueLinks').click()
                except:
                    try:
                        time.sleep(2)
                        driver.find_element_by_class_name('taLnk.ulBlueLinks').click()
                    except:
                        print("cannot expand comments")
                
            # grab container and append to list
            page_obj = bs4.BeautifulSoup(driver.page_source, "html.parser")
            page = page_obj.select("#taplc_location_reviews_list_responsive_detail_0")
            pages.append(page[0])
            # print(page[0].text.translate(non_bmp_map)) # uncomment this line if emojis are causing print problems

            print("Page %s of %s complete" % (count, last))
            
            # advance page
            try:
                driver.find_element_by_class_name('next').click()
            except:
                try:
                    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")))
                    driver.find_element_by_class_name('next').click()
                except:
                    try:
                        time.sleep(2)
                        driver.find_element_by_class_name('next').click()
                    except:
                        logError(filename, count, last)
                        break

            count += 1
                
    driver.close()
    
    # write results to a file
    writePyxl.write(pages, filename)

if __name__ == "__main__":

    url = "https://www.tripadvisor.com/Attraction_Review-g294201-d553185-Reviews-Keops_Pyramid-Cairo_Cairo_Governorate.html"
    GetComments(url)
    
