from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self._driver = driver

    def result(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label').text
        return total
