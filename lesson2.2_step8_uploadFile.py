from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstNameInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'First name*')]/following::input[1] ")
    firstNameInput.send_keys("Name")

    lastNameInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Last name*')]/following::input[1]")
    lastNameInput.send_keys("LastName")

    emailInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Email *')]/following::input[1]")
    emailInput.send_keys("email@test.com")


    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    attachFileInput = browser.find_element(By.ID, "file")
    attachFileInput.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()