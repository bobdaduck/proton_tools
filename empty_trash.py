#############################
# Protonmail free tier does not automatically empty the trash. This utility walks through the trash folder and permanently delete all items.
# 2023 bobdaduck
####################
from Pages import pages

from Pages.inbox import Inbox
from Pages.trash import Trash
from browser import Driver

class Begin():

    driver = Driver().get_instance()
    trash = Trash(driver)
    trash.goto()
    for i in range(trash.total_pages):
        trash.select_all.click()
        trash.delete_permanently.click()
        trash.delete_confirmation.click()
    driver.quit()
    
    

if __name__ == '__main__':
    Begin()
