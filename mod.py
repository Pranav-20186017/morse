from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import os
from os import listdir
from os.path import isfile, join
download_path = "C:\\Users\\spsk9\\Downloads"
driver = webdriver.Chrome()
driver.get("https://morsecode.scphillips.com/translator.html")
elem = driver.find_element_by_xpath('//*[@id="input"]')
f = open("words.txt","r")
for text in f:
	new_file = text.strip("\n") + ".wav"
	elem.send_keys(text)
	time.sleep(1)
	button = driver.find_element_by_xpath('//*[@id="download"]')
	button.click()
	time.sleep(1.5)
	elem.clear()
	subs = "morse"
	onlyfiles = [f for f in listdir(download_path) if isfile(join(download_path, f))]
	res = [i for i in onlyfiles if subs in i] 
	os.rename(res[0], new_file)
driver.quit()
print("Done")
