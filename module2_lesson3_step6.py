from selenium import webdriver
import time
import math
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(4)
    browser.quit()