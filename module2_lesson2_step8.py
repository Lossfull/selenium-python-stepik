from selenium import webdriver
import time
import os 
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("div.form-group input.form-control[placeholder='Enter first name']")
    element2 = browser.find_element_by_css_selector("div.form-group input.form-control[placeholder='Enter last name']")
    element3 = browser.find_element_by_css_selector("div.form-group input.form-control[placeholder='Enter email']")
    required_elements = [element1, element2, element3]
    for element in required_elements:
        element.send_keys("Мой ответ")
        

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'empty.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()