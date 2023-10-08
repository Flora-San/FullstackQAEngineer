import time

from selenium.webdriver.common.by import By

from Locators.Locators import HomePageLocators, ProductPageLocators


def capture_screenshot(browser, filename):
    try:
        browser.save_screenshot(filename)
        return True
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")
        return False


def search_hats_men(browser):
    search_box = browser.find_element(*HomePageLocators.SEARCH_BOX)
    search_box.click()
    search_box.send_keys("hats for men")
    search_icon = browser.find_element(*HomePageLocators.SEARCH_ICON)
    search_icon.click()
    time.sleep(3)

    element = browser.execute_script('return document.querySelector(".a-section.a-spacing-base");')
    element.click()
    time.sleep(1)


def search_hats_woman(browser):
    search_box = browser.find_element(*HomePageLocators.SEARCH_BOX)
    search_box.click()
    search_box.send_keys("hats for women")
    search_icon = browser.find_element(*HomePageLocators.SEARCH_ICON)
    search_icon.click()
    time.sleep(3)

    element = browser.execute_script('return document.querySelector(".a-section.a-spacing-base");')
    element.click()
    time.sleep(1)

