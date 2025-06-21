#############################
# Protonmail free tier does not let you set up "inbound rules". 
# 2025 bobdaduck
####################
from Pages import pages

from Pages.inbox import Inbox
from Pages.trash import Trash
from browser import Driver
from personal_rules import email_folders



class Begin():

    driver = Driver().get_instance()
    inbox = Inbox(driver)
    inbox.goto()

    for key, value in email_folders.items():
        for item in inbox.page_items():
            if item.header == key:
                item.checkbox.click()
        inbox.move_to_folder(value)

    driver.quit()
    
if __name__ == '__main__':
    Begin()
