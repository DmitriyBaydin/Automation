from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def fill_form(self):
        self._driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Natalya")
        self._driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Baydina")
        self._driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("140013")
        self._driver.find_element(By.XPATH, '//*[@id="continue"]').click()
