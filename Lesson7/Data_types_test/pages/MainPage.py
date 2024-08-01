from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_first_name(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def fill_last_name(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def fill_address(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def fill_zip_code(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    def fill_city(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def fill_country(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def fill_email(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def fill_phone(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def fill_job_position(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def fill_company(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    def submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[type="submit"]').click()
