from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # нажать кнопку Add button 5 раз
    for v in range(5):
        # add button
        add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)

        # collect Delete buttons
        chrome_delete_buttons = chrome.find_elements(
            By.XPATH, '//button[text()="Delete"]')
        firefox_delete_buttons = firefox.find_elements(
            By.XPATH, '//button[text()="Delete"]')


except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()

# print length list
print(f"размер списка Delete в Chrome: {len(chrome_delete_buttons)}")
print(f"размер списка Delete в Firefox: {len(firefox_delete_buttons)}")
