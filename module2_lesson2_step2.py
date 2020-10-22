from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	summary = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
	
	dropdown = browser.find_element_by_id("dropdown")
	select = Select(dropdown)
	select.select_by_value(str(summary))
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
finally:
	time.sleep(3)
	browser.quit()