from typing import Union


from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from utilities.configreader import *
import time
from datetime import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
import logging
from utilities.log_utility import Logger

log = Logger(__name__, logging.INFO)


class BasePage: 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        

    def wait_for_page_to_load(self):
        """
        Waits for the page to be fully loaded by checking the document.readyState.
        """
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    def wait_for_element_to_be_visible(self, by, value):
        """
        Waits for an element to be visible on the page.
        """
        self.wait.until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_for_element_to_be_clickable(self, by, value):
        """
        Waits for an element to be clickable.
        """
        self.wait.until(
            EC.element_to_be_clickable((by, value))

        )


    def iselementPresent(self, how, what):
        try:
            self.driver.find_element(by=how, value=readConfig("locators", what))
            return True
        except NoSuchElementException:
            return False



    def get_text(self, locator):
        global gettext
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        gettext=self.driver.find_element(By.XPATH, readConfig("locators", locator))
        print("Text for clicked element is: ", gettext.text)

        return gettext.text
    
    def capture_screenshot(self, request):
        
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

    # 🧹 Delete old screenshots
        for file in os.listdir(screenshots_dir):
            file_path = os.path.join(screenshots_dir, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"❌ Could not delete: {e}")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        item = request.node
        test_name = item.name.replace(" ", "_")
        Filename = f"screenshots/{test_name}_{timestamp}.png"

        self.driver.save_screenshot(Filename)


    def selector(self, locator):
        global elem
        if str(locator).endswith("_XATH"):
            elem=self.driver.find_element(By.XPATH, readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
           elem= self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            elem=self.driver.find_element(By.ID, readConfig("locators", locator))
        return elem

    def click(self, locator):

        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, readConfig("locators", locator)).click()
        log.logger.info(f"Clicked element is: {locator}")

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, readConfig("locators", locator)).send_keys(value)
        log.logger.info(f" Typed element is: {locator} and value is: {value}")

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)

    def moveTo(self, locator):
        global element
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).context_click().perform()
        log.logger.info(f"Moved to element is: {element}")

    def js_scroll(self, times,pause_time):
        self.driver.execute_script("window.focus();")

        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(pause_time)
    
    # Wait for page load
    def wait_for_page_ready(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete') 
        
    def highlight_element(self, locator):
        highlight= self.driver.find_element(By.XPATH, readConfig("locators", locator))
        self.driver.execute_script("arguments[0].style.border= '3px dotted red'", highlight)
        self.driver.execute_script("arguments[0].style.backgroundColor= 'yellow'", highlight)
        log.logger.info(f"Highlighted element is: {locator}")

    def submit(self, webelement: WebElement) -> None:
        self.highlight_element(webelement)
        webelement.submit()

