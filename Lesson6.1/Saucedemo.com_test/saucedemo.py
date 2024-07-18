from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("https://www.saucedemo.com/")

browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
browser.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
browser.find_element(By.CSS_SELECTOR, "#login-button").click()
sleep(5)
browser.find_element(
    By.XPATH, '// *[@id="add-to-cart-sauce-labs-backpack"]').click()
browser.find_element(
    By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
browser.find_element(
    By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
sleep(2)
browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
sleep(2)
browser.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Natalya")
browser.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Baydina")
browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("140013")
browser.find_element(By.XPATH, '//*[@id="continue"]').click()
sleep(2)

Total = browser.find_element(
    By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
print(Total + "$")
browser.quit()
