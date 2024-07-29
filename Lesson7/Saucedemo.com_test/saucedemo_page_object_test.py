from selenium import webdriver
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from pages.CheckoutPage import CheckoutPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_buying():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.user_login("standard_user")
    main_page.user_pass("secret_sauce")
    main_page.user_submit()

    product_page = ProductPage(browser)
    added = product_page.add_product()

    cart_page = CartPage(browser)
    checkout = cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    fill_form = checkout_page.fill_form()

    result_page = ResultPage(browser)

    assert "Total: $58.29" == result_page.result()
