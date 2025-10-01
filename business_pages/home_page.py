import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from selenium.webdriver.common.keys import Keys
from business_pages.base_page import BasePage
from business_pages.starcraft2_streamer_page import StreamerPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.configreader import *


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        




    def click_search(self):
        self.wait_for_page_to_load()
        #clicking on search box
        self.click("search_input_box_XPATH")


    def enter_text(self, text: str):
        #entering search text in search box
        self.type("search_input_box_XPATH", text)
        #highlighting search button
        self.highlight_element("search_button_XPATH")
        #clicking on search button
        self.click("search_button_XPATH")
        #Wait for the search results page to load
        self.wait_for_page_to_load()
        #returning StreamerPage object to navigate to next page
        return StreamerPage(self.driver)
        