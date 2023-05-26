from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"


try:
   # test_input_text(8, 11)
   # test_input_text(11, 11)
    test_input_text(11, 15)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    f"Something went wrong"

