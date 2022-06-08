from selenium.webdriver.common.by import By

from constants.base import SIGN_IN


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SearchTextElement:
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class MainPage(BasePage):
    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def click_button(self):
        """Triggers the search"""
        element = self.driver.find_element(By.ID, SIGN_IN)
        element.click()
