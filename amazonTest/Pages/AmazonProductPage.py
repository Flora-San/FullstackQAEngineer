import time

from Locators.Locators import HomePageLocators, ProductPageLocators


def add_to_cart(browser):
    add_hat_men = browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
    add_hat_men.click()
    time.sleep(2)


def add_to_cart_women(browser):
    add_hat_women = browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
    add_hat_women.click()
    time.sleep(2)
