
from selenium.webdriver.common.by import By
from browser import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Trash:

    def __init__(self, driver):
        self.driver = driver
        self.lower_pagination_first_locator = (By.CSS_SELECTOR, "[data-testid='pagination-row:go-to-first-page']")
        self.page_number_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:page-number-dropdown']")

        self.select_all_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:select-all-checkbox']")
        self.page_next_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:next-page']")
        self.delete_permanently_locator = (By.CSS_SELECTOR, "[data-testid='toolbar:deletepermanently']")
        self.delete_confirmation_locator = (By.CSS_SELECTOR, "[data-testid='permanent-delete-modal:submit']")
        

    @property
    def page_next(self):
        return self.driver.find_element(*self.page_next_locator)

    @property
    def delete_permanently(self):
        return self.driver.find_element(*self.delete_permanently_locator)

    @property
    def delete_confirmation(self):
        return self.driver.find_element(*self.delete_confirmation_locator)

    @property
    def select_all(self):
        self.driver.find_element(*self.lower_pagination_first_locator) # Todo: Find a different locator for verifying proton is caught up, this element is not loaded if there's only one page.
        return self.driver.find_element(*self.select_all_locator)

    @property
    def page_number(self): 
        return self.driver.find_element(*self.page_number_locator) 

    @property
    def total_pages(self):  
        _, total_pages = self.page_number.text.split("/") 
        return int(total_pages)


    def goto(self):
        self.driver.get("https://mail.proton.me/u/0/trash")