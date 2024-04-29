
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.XPATH, '//input[@name="username"]'))
        username_input.send_keys(username)
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.XPATH, '//input[@name="password"]'))
        password_input.send_keys(password)
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//button[@type="submit"]'))
        login_button.click()

