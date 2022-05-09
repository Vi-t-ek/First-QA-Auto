import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_start_page(self):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Cleaning login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()

        # Clear field password
        self.log.info("Cleaning password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / password", "Text is not valid"

        # Close driver
        driver.close()
