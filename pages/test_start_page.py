import logging
import random
import string


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions

from constants.base import SIGN_IN, DRIVER_PATH, BASE_URL, ERROR_MESSAGE_LOGIN, REGISTER_LOGIN, REGISTER_SIGN_UP_BUTTON, \
    REGISTER_PASSWORD, PASSWORD, ERROR_MESSAGE_MAIL


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_empty_fields_login(self):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(DRIVER_PATH)
        driver.implicitly_wait(15)

        # Open start page
        self.log.info("Opening start page")
        driver.get(BASE_URL)

        self.log.info("Going to click 'Sign In' button")

        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=SIGN_IN).click()

        error_message = driver.find_element(by=By.XPATH, value=ERROR_MESSAGE_LOGIN)
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    def test_invalid_mail(self):
        """
        - Create driver
        - Open start page
        - Fill field username
        - Fill field password
        - Click on 'Sign Up' button
        - Verify error message mail
        """
        # Create driver
        driver = WebDriver(DRIVER_PATH)
        driver.implicitly_wait(15)
        # Open start page
        self.log.info("Opening start page")
        driver.get(BASE_URL)

        # Clear field login
        self.log.info("Filling login field")
        # - Find element
        login_field = driver.find_element(By.XPATH, REGISTER_LOGIN)
        # - Clear
        login_field.clear()
        login_field.send_keys("RandomName13")

        # - Fill
        # Clear field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(By.XPATH, REGISTER_PASSWORD)
        # - Clear
        password_field.clear()
        # - Fill
        password_field.send_keys(PASSWORD)

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(By.XPATH, REGISTER_SIGN_UP_BUTTON).click()

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(By.XPATH, ERROR_MESSAGE_MAIL)
        assert error_message.text == "You must provide a valid email address.", "Text is not valid"

        # Close driver
        driver.close()

    # """Generate random string"""
    #     return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    #
    #
    # def wait_until_clickable(self, xpath):
    # """Waits until element is clickable"""
    #     return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
    #
    #
    # def wait_until_displayed(self, xpath):
    #     """Waits until element is displayed"""
    #     return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
    #
    #
    # def is_element_exists(self, xpath):
    # """Check if element exists"""
    #     try:
    #         self.driver.find_element(by=By.XPATH, value=xpath)
    #         return True
    #     except (TimeoutError, NoSuchElementException):
    #         return False
    #
    #
    # def fill_field(self, xpath, value):
    #     """Send data into the field"""
    #     field = self.wait_until_clickable(xpath)
    #     field.clear()
    #     field.send_keys(value)
    #
    #
    # def click(self, xpath):
    #     """Find and click the element"""
    #     self.wait_until_clickable(xpath).click()
    # def test_register(self):
    #     """
    #     - Open start page
    #     - Fill email, login and password fields
    #     - Click on Sign Up button
    #     - Verify registration is successful
    #     """
    #     # Create driver
    #     driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")
    #
    #     # Open start page
    #     driver.get("https://qa-complex-app-for-testing.herokuapp.com")
    #     self.log.debug("Open page")
    #
    #     # Fill username
    #     user = self.random_str()
    #     username_value = f"{user}{self.random_num()}"
    #     username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
    #     username.clear()
    #     username.send_keys(username_value)
    #
    #     # Fill email
    #     email_value = f"{user}{self.random_num()}@mail.com"
    #     email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
    #     email.clear()
    #     email.send_keys(email_value)
    #
    #     # Fill password
    #     password_value = f"{self.random_str(6)}{self.random_num()}"
    #     password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
    #     password.clear()
    #     password.send_keys(password_value)
    #     self.log.info("Fields were filled")
    #     sleep(1)
    #
    #     # Click on Sign Up button
    #     driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
    #     self.log.info("User was registered")
    #     sleep(1)
    #
    #     # Verify register success
    #     hello_message = driver.find_element(by=By.XPATH, value=".//h2")
    #     assert username_value.lower() in hello_message.text
    #     assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
    #     assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
    #     self.log.info("Registration for user '%s' was success and verified", username_value)
