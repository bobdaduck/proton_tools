from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Driver:

    def __init__(self):
                
        service = Service()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=C:/Users/bobdaduck/AppData/Local/Google/Chrome/User Data/Default") # Neat trick, use system cookies so selenium doesn't have to login
        chrome_options.add_argument("start-maximized") #  open Browser in maximized mode
        chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(40) # twitter is SLOW on chromedriver

    def get_instance(self):
        return self.driver
    
