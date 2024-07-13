import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    wait_ch = WebDriverWait(chrome, 10)
    wait_f = WebDriverWait(firefox, 10)
    modal_ch_window = wait_ch.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".modal")))
    modal_f_window = wait_f.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".modal")))
    close_ch_button = wait_ch.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, ".modal-footer")))
    close_f_button = wait_f.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_ch_button.click()
    close_f_button.click()
    time.sleep(2)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
