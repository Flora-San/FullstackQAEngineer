import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# clear cache
CHROMEDRIVER = Path('chromedriver.exe')


# def start_driver():
#     driver = webdriver.Chrome(executable_path=str(CHROMEDRIVER))
#     delete_cache(driver)
#     return driver


def delete_cache(driver):
    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('chrome://settings/clearBrowserData')
    perform_actions(driver,
                    Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)
    driver.close()
    driver.switch_to.window(
        driver.window_handles[0])


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    print('Performing Actions!')
    actions.perform()

# if __name__ == '__main__':
