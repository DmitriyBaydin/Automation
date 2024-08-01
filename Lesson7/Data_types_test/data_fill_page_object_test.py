from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


def test_data_fill():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.fill_first_name("Иван")
    main_page.fill_last_name("Петров")
    main_page.fill_address("Ленина, 55-3")
    main_page.fill_zip_code("")
    main_page.fill_city("Москва")
    main_page.fill_country("Россия")
    main_page.fill_email("test@skypro.com")
    main_page.fill_phone("+7985899998787")
    main_page.fill_job_position("QA")
    main_page.fill_company("SkyPro")
    main_page.submit()

    result_page = ResultPage(browser)

    assert "rgba(132, 32, 41, 1)" in result_page.red_color()

    assert "rgba(15, 81, 50, 1)" in result_page.green_color()
