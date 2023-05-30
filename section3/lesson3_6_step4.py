import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_entering_answers(browser, link):

    browser.get(link)

    #Нажимаем кнопку "Войти"
    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]"))
    )
    browser.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()

    # нажимаем таб "Войти"
    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-tab-name = login]"))
    )
    browser.find_element(By.CSS_SELECTOR, "a[data-tab-name = login]").click()

    browser.find_element(By.XPATH, "//input[@name='login']").send_keys("LOGIN")
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys("PASSWORD")
    browser.find_element(By.XPATH, "//button[text()='Войти']").click()

    time.sleep(3)

    answer = math.log(int(time.time()))

    WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea"))
    )

    if browser.find_element(By.XPATH, "//textarea").get_attribute("disabled"):
        browser.find_element(By.XPATH, "//button[text()='Решить снова']").click()
        WebDriverWait(browser, 12).until_not(
            EC.element_attribute_to_include((By.XPATH, "//textarea"), "disabled")
        )


    browser.find_element(By.XPATH, "//textarea").send_keys(answer)
    browser.find_element(By.XPATH, "//button[text()='Отправить']").click()

    WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")

    messageText = message.text
    assert "Correct!" == messageText, \
        f"expected 'Correct!', got {messageText}"