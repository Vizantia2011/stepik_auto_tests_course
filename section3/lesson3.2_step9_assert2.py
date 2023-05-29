from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_substring(full_string, substring):
    assert substring in full_string , f"expected {substring} to be substring of {full_string}"


try:
    test_substring("fulltext", "some_value")
   # test_substring(11, 11)
   # test_substring("11", "15")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    f"Something went wrong"

