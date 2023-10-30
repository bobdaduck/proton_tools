#############################
# Protonmail free tier only allows one filter. This utility crawls inbox and sorts emails according to the email_keys file.
# 2023 bobdaduck
####################
from Pages.inbox import Inbox
from browser import Driver
from sort_emails_key import Folder1Addresses, Folder2Addresses, Folder3Addresses, AutoTrashAddresses

class Begin():

    driver = Driver().get_instance()
    inbox = Inbox(driver)
    inbox.goto()
    for i in range(inbox.total_pages): #still undecided on whether to use search or crawl
        pass
    
    driver.quit()
    
    

if __name__ == '__main__':
    Begin()
