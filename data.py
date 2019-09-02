from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def download(text):
	options = webdriver.ChromeOptions() 
	# options.add_argument("download.default_directory = C:\\Users\\spsk9\\Desktop\\morse\\data")
	options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options = options)
	driver = webdriver.Chrome()
	driver.get("https://morsecode.scphillips.com/translator.html")
	#element = '//*[@id="input"]'
	elem = driver.find_element_by_xpath('//*[@id="input"]')
	elem.send_keys(text)
	time.sleep(1)
	button = driver.find_element_by_xpath('//*[@id="download"]')
	button.click()
	time.sleep(3)
	driver.close()

def main():
	f = open("words.txt","r")
	for x in f:
		download(x)
		print(x + "downloaded")

if __name__ == '__main__':
	main()