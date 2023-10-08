import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v115.cache_storage import delete_cache

from Pages.AmazonCartPage import assert_quantity, assert_price
from Pages.AmazonHomePage import search_hats_woman, search_hats_men
from Pages.AmazonProductPage import add_to_cart_women, add_to_cart

AMAZON_URL = "https://www.amazon.com"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_amazon(browser):
    browser.get(AMAZON_URL)
    browser.save_screenshot("screenshots/test_women/successful_open_page.png")
    search_hats_woman(browser)
    browser.save_screenshot("screenshots/test_women/successful_search_hats_women.png")


def test_change_quantity_women(browser):
    browser.get(AMAZON_URL)
    search_hats_woman(browser)
    add_to_cart_women(browser)
    browser.save_screenshot("screenshots/test_women/women_hats_added_cart.png")
    assert_price(browser)
    browser.save_screenshot("screenshots/test_women/assert_price_women_hats.png")


def test_change_quantity_men(browser):
    browser.get(AMAZON_URL)
    search_hats_woman(browser)
    add_to_cart_women(browser)
    search_hats_men(browser)
    add_to_cart(browser)
    browser.save_screenshot("screenshots/test_men/men_hats_added_cart.png")
    assert_price(browser)
    browser.save_screenshot("screenshots/test_men/assert_price_men_hats.png")
    assert_quantity(browser)
    browser.save_screenshot("screenshots/test_men/assert_quantity_men_hats.png")


if __name__ == "__main__":
    pytest.main(["-v", "test_amazon.py"])
