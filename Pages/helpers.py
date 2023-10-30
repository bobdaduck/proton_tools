from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time  # bad practice frontend, okay practice for writing helper functions
from selenium.webdriver.support import expected_conditions as EC


def find_element_by_class_then_text(driver, class_name, desired_text):
    time.sleep(5)
    elements = driver.find_elements_by_class_name(class_name)
    for web_element in elements:
        text = web_element.text
        if text == desired_text:
            return web_element
    raise Exception("no elements with class_name " + class_name + " have text " + desired_text)


def wait_for_loading_overlay(driver):
    while True:
        try:
            driver.find_elements_by_class_name("modal-two")
        except:
            break


def try_clicking_for_duration(element, duration):
    for x in range(0, duration):
        try:
            element.click()
            break
        except:  # todo: make instance of ElementClickInterceptedException:
            time.sleep(1)

def wait_for_element(driver, locator_definition): 
    #WebDriverWait(driver, 20).until(
     #           EC.visibility_of_element_located(locator_definition)
      #      )
    WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(locator_definition)
            )