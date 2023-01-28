from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Guru99LoginPage:
    URL = 'https://demo.guru99.com/V1/index.php'
    UserID_input = (By.XPATH, '//tbody/tr[1]/td[2]/input[1]')
    Password_input = (By.XPATH, '//tbody/tr[2]/td[2]/input[1]')
    LOGIN_BUTTON = (By.XPATH, '//tbody/tr[3]/td[2]/input[1]')
    RESET_BUTTON = (By.XPATH, '//tbody/tr[3]/td[2]/input[2]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@id="save"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, userid, password):
        # self.browser.find_element(*self.ACCEPT_COOKIES).click()
        user_input = self.browser.find_element(*self.UserID_input)
        user_input.send_keys(userid)
        password_input = self.browser.find_element(*self.Password_input)
        password_input.send_keys(password + Keys.RETURN)
        # login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        # login_button.click()

    def title_source(self):
        return self.browser.title, self.browser.page_source

    def alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        return alert_text
