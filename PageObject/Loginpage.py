from selenium.webdriver.common.by import By


class Loginpage:
    username = "email"
    password = "password"
    buttonlogin = "body > app-root > app-signin > div > div.right-side > form > button"

    def __init__(self, driver):
        assert isinstance(driver, object)
        self.driver = driver

    def EnterUserName(self, username):
        try:
            username_element = self.driver.find_element(By.ID, self.username)
            username_element.send_keys(username)
        except Exception as Failed:
            print(f"username: {Failed}")

    def EnterPassword(self, password):
        try:
            password_element = self.driver.find_element(By.ID, self.password)
            password_element.send_keys(password)
        except Exception as Failed:
            print(f"Password: {Failed}")

    def ClickLogin(self):
        try:
            login_button = self.driver.find_element(By.CSS_SELECTOR, self.buttonlogin)
            login_button.click()
        except Exception as Failed:
            print(f"button: {Failed}")
