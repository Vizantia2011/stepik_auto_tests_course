from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(y)

    checkBoxImRobot = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    checkBoxImRobot.click()

    radioButtonRobo = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    radioButtonRobo.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
