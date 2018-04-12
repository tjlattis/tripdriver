#! usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import traceback

driver = webdriver.Firefox()
url = "https://www.tripadvisor.com/Attractions-g294201-Activities-c47-Cairo_Cairo_Governorate.html#FILTERED_LIST"
driver.get(url)

# id="AL_LIST_CONTAINER"
