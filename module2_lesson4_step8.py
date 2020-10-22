from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    condition = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 
    button = browser.find_element_by_css_selector("button.btn#book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn#solve")
    button.click()
    
finally:
    time.sleep(4)
    browser.quit()