from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_1(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def fill_2(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def fill_3(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def fill_4(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    def fill_5(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def fill_6(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def fill_7(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def fill_8(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def fill_9(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def fill_10(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    def submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[type="submit"]').click()
