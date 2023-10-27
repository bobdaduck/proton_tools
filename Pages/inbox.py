
from selenium.webdriver.common.by import By
from browser import Driver


class Inbox:

    def __init__(self, driver):
        self.driver = Driver().get_instance()

    def goto(self):
        self.driver.get("https://mail.proton.me/")
