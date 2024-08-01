from selenium import webdriver
from pages.MainPage import MainPage


def test_calc_fill():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_delay("45")
    main_page.perform_operations()
    main_page.wait(46)
    total = main_page.total()

    assert 15 == total
