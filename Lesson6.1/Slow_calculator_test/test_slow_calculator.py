import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    browser.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    browser.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    browser.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    browser.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    waiter = WebDriverWait(browser, 60)

    waiter.until(
        EC.text_to_be_present_in_element((
            By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15")
        )

    result = browser.find_element(
        By.XPATH, '//*[@id="calculator"]/div[1]/div').text
    assert "15" in result

    browser.quit()
