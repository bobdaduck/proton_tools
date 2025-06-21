
from selenium.webdriver.common.by import By
from browser import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inbox:

    def __init__(self, driver):
        self.driver = driver

        self.lower_pagination_first_locator = (By.CSS_SELECTOR, "[data-testid='pagination-row:go-to-first-page']")
        self.item_locator = (By.CSS_SELECTOR, "[data-shortcut-target='item-container']")
        self.item_header_locator = (By.CSS_SELECTOR, "[data-shortcut-target='message-column:sender-address']") 


    def goto(self):
        self.driver.get("https://mail.proton.me/")

    @property
    def page_next(self):
        return self.driver.find_element(*self.page_next_locator)

@property
def page_items(self):
    items = self.driver.find_elements(*self.item_locator)
    email_items = []
    
    for item in items:
        email_item = type('obj', (object,), {
            'web_element': item,
            'header': item.find_element(*self.item_header_locator).find_element(*self.item_header_locator).text, 
            # 'checkbox': checkbox 
        })
        email_items.append(email_item)
    
    return email_items
