from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    for v in range(3):
            
            chrome.get("http://uitestingplayground.com/classattr")
            firefox.get("http://uitestingplayground.com/classattr")

            blue_chrome_button = chrome.find_element(
                By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
            blue_firefox_button = firefox.find_element(
                By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
            sleep(5)

            chrome.switch_to.alert.accept()
            firefox.switch_to.alert.accept()

            chrome.refresh()
            firefox.refresh()

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
