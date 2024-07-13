from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
try:
    for _ in range(3):
        chrome.get("http://uitestingplayground.com/dynamicid")
        firefox.get("http://uitestingplayground.com/dynamicid")

        blue_chrome_button = chrome.find_element(
            By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
        blue_firefox_button = firefox.find_element(
            By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
        sleep(5)
        chrome.refresh()
        firefox.refresh()

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
