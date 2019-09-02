from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\spsk9\\Desktop\\morse\\data"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\chrome"
driver = webdriver.Chrome(executable_path = chromedriver, chrome_options = chromeOptions)
driver.get("https://morsecode.scphillips.com/translator.html")
elem = driver.find_element_by_xpath('//*[@id="input"]')
elem.send_keys("alfa")
button = driver.find_element_by_xpath('//*[@id="download"]')
button.click()
time.sleep(3)
driver.close()
