import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v115.cache_storage import delete_cache

from Pages.AmazonHomePage import search_hats_men
from Pages.AmazonProductPage import add_to_cart
from Pages.AmazonCartPage import change_quantity_hats, assert_price

AMAZON_URL = "https://www.amazon.com"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_amazon(browser):
    browser.get(AMAZON_URL)
    browser.save_screenshot("screenshots/test_men/successful_open_page.png")
    search_hats_men(browser)
    browser.save_screenshot("screenshots/test_men/successful_search_hats.png")


def test_change_quantity(browser):
    browser.get(AMAZON_URL)
    search_hats_men(browser)
    change_quantity_hats(browser)
    add_to_cart(browser)
    browser.save_screenshot("screenshots/test_men/men_hats_added_cart.png")
    assert_price(browser)
    browser.save_screenshot("screenshots/test_men/assert_price_men_hats.png")


if __name__ == "__main__":
    pytest.main(["-v", "test_amazon.py"])
