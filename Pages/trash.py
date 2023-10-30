
from selenium.webdriver.common.by import By
from browser import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.helpers import wait_for_element
from Pages.helpers import wait_for_loading_overlay

class Trash:

    def __init__(self, driver):
        self.driver = driver
        self.page_next_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:next-page']")
        self.delete_permanently_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:deletepermanently']")
        self.delete_confirmation_locator = (By.CSS_SELECTOR, "[data-testid='permanent-delete-modal:submit']")
        self.select_all_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:select-all-checkbox']")

    @property
    def page_next(self):
        return self.driver.find_element(*self.page_next_locator)

    @property
    def delete_permanently(self):
        return self.driver.find_element(*self.delete_permanently_locator)

    @property
    def delete_confirmation(self):
        # wait_for_element(self.driver, self.delete_confirmation_locator)
        wait_for_loading_overlay(self.driver)
        return self.driver.find_element(*self.delete_confirmation_locator)

    @property
    def select_all(self):
        return self.driver.find_element(*self.select_all_locator)
    
    # self.trash_locator = (By_data_testid, "navigation-link:trash")


    def goto(self):
        self.driver.get("https://mail.proton.me/u/0/trash")