import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from Locators.Locators import HomePageLocators, ProductPageLocators


def change_quantity_hats(browser):
    quantity = browser.execute_script('return document.querySelector(".a-button.a-button-dropdown.a-button-small");')
    quantity.click()
    time.sleep(2)
    add_quantity = browser.find_element(*ProductPageLocators.ID_QUANTITY)
    add_quantity.click()
    time.sleep(2)


def change_quantity_hats_women(browser):
    quantity = browser.execute_script('return document.querySelector(".a-button.a-button-dropdown.a-button-small");')
    quantity.click()
    time.sleep(2)
    add_quantity = browser.find_element(*ProductPageLocators.ID_QUANTITY_WOMEN)
    add_quantity.click()
    time.sleep(2)


def assert_price(browser):
    price_element = browser.find_element(By.CLASS_NAME, 'a-price.sw-subtotal-amount')
    price_text = price_element.text
    expected_price = price_text
    assert price_text == expected_price, f"Expected price: {expected_price}, Actual price: {price_text}"


def assert_quantity(browser):
    quantity_element = browser.find_element(By.CLASS_NAME, 'sc-subtotal-label-buybox')
    quantity_text = quantity_element.text
    expected_quantity = quantity_text
    assert quantity_text == expected_quantity, f"Expected quantity: {expected_quantity}, Actual quantity: {quantity_text}"

