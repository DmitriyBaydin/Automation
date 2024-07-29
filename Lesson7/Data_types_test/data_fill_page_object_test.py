from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


def test_data_fill():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.fill_1("Иван")
    main_page.fill_2("Петров")
    main_page.fill_3("Ленина, 55-3")
    main_page.fill_4("")
    main_page.fill_5("Москва")
    main_page.fill_6("Россия")
    main_page.fill_7("test@skypro.com")
    main_page.fill_8("+7985899998787")
    main_page.fill_9("QA")
    main_page.fill_10("SkyPro")
    main_page.submit()

    result_page = ResultPage(browser)

    assert "rgba(132, 32, 41, 1)" in result_page.red_color()

    assert "rgba(15, 81, 50, 1)" in result_page.green_color()
