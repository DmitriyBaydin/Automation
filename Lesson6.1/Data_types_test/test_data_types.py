import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_fill_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    browser.find_element(
        By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    browser.find_element(
        By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    browser.find_element(
        By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    browser.find_element(
        By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    browser.find_element(
        By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    browser.find_element(
        By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    browser.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    browser.find_element(
        By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    browser.find_element(
        By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    browser.find_element(
        By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    browser.find_element(
        By.CSS_SELECTOR, '[type="submit"]').click()

    assert "rgba(132, 32, 41, 1)" in browser.find_element(
        By.CSS_SELECTOR, "div.alert-danger").value_of_css_property("color")

    other_fields = browser.find_elements(By.CSS_SELECTOR, "div.alert-success")
    for field in other_fields:
        assert "rgba(15, 81, 50, 1)" in browser.find_element(
            By.CSS_SELECTOR, "div.alert-success").value_of_css_property("color")

    browser.quit()
