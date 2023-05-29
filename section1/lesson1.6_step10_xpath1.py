from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstNameInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'First name*')]/following::input[1] ")
    firstNameInput.send_keys("Name")

    lastNameInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Last name*')]/following::input[1] ")
    lastNameInput.send_keys("LastName")

    emailInput = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Email*')]/following::input[1] ")
    emailInput.send_keys("email@test.com")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()