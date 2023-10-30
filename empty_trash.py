from Pages import pages

from Pages.inbox import Inbox
from Pages.trash import Trash
from browser import Driver

class Begin():
    driver = Driver().get_instance()
    trash = Trash(driver)
    trash.goto()
    trash.select_all.click()
    trash.delete_permanently.click()
    trash.delete_confirmation.click()
    # trash.page_next.click()
    input()

if __name__ == '__main__':
    Begin()
