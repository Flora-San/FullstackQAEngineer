from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, "nav-search-submit-button")
    FIRST_RESULT = (By.XPATH, "//*[@id=search]/div[1]/div[1]/div/span[1]/div[1]/div[2]")


class ProductPageLocators:
    STOCK = (By.ID, "availability")
    QUANTITY_DROPBOX = (By.ID, "outOfCountryInsideBuyBox_feature_div")
    ID_QUANTITY = (By.ID, "quantity_1")
    ID_QUANTITY_WOMEN = (By.ID, "quantity_0")
    ADD_CART_BUTTON = (By.ID, "add-to-cart-button")


class CartPageLocators:
    SUBTOTAL_ITEMS = (By.ID, "sc-subtotal-label-buybox")
    SUBTOTAL_AMOUNT = (By.ID, "sc-subtotal-amount-buybox")
    TWO_HATS_MEN = "2"
