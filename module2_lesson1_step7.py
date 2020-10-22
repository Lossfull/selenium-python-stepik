from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    picture = browser.find_element_by_id("treasure")
    treasure = picture.get_attribute("valuex")
    #x_element = treasure
    x = treasure
    y = str(math.log(abs(12*math.sin(int(x)))))
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('input[value="robots"]')
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(10)
	browser.quit()