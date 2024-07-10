from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")

    count_ch = 0
    count_f = 0
    blue_chrome_button = chrome.find_element(
        By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
    blue_firefox_button = firefox.find_element(
        By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
    # press button 3
    for v in range(3):
        blue_chrome_button = chrome.find_element(
            By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
        blue_firefox_button = firefox.find_element(
            By.XPATH, '// button[text()="Button with Dynamic ID"]').click()
        count_chrome = count_ch + 1
        count_firefox = count_f + 1
        sleep(2)
        print("count Chrome:", count_chrome)
        print("count Firefox:", count_firefox)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
