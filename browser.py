from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Driver:

    def __init__(self):
                
        service = Service()
        # options=options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=C:/Users/bobdaduck/AppData/Local/Google/Chrome/User Data/Default") # Neat trick, use system cookies so selenium doesn't have to login
        chrome_options.add_argument("start-maximized") #  open Browser maximized 
        chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

        self.driver = webdriver.Chrome(service=service,options=chrome_options)
        self.driver.implicitly_wait(10) 
    
        
    def get_instance(self):
        return self.driver
    
