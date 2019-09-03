from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://morsecode.scphillips.com/translator.html")
elem = driver.find_element_by_xpath('//*[@id="input"]')
f = open("words.txt","r")
for text in f:
	elem.send_keys(text)
	time.sleep(1)
	button = driver.find_element_by_xpath('//*[@id="download"]')
	button.click()
	time.sleep(2)
	elem.clear()
print("Done")