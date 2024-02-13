from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def test_guest_can_go_to_login_page(self):
        link = "http://selenium1py.pythonanywhere.com/"
        self.browser.get(link)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
