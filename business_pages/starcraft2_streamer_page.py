from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from utilities.configreader import *
from selenium.common.exceptions import TimeoutException
from business_pages.base_page import BasePage
import time 


class StreamerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def scroll_down_times(self):

        #Scrolling down the page to load more videos
        self.click("show_all_videos_button_XPATH")
        #Hardcoding sleep to see the scroll effect
        time.sleep(2)
        el = self.driver.find_element(By.CSS_SELECTOR, readConfig("locators", "scrollable_area_CSS"))
        self.driver.execute_script("arguments[0].scrollTop += 400;", el)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollTop += 400;", el)
        
        
        
        
    def click_one_streamer(self):
        #Clicking on one of the streamers from the block of videos after scrolling down
        videos_list=self.driver.find_elements(By.CSS_SELECTOR, readConfig("locators", "streamer_videos_block_CSS"))
        if len(videos_list) > 0:
            videos_list[0].click()
            time.sleep(5)

    def check_for_modal(self, request):
        # Wait for the page to be fully loaded
        self.wait_for_page_ready()

        try:
        #Try to find the "subscribers-only" message
            sub_only_banner = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//strong[contains(text(),'only available to subscribers') or contains(text(),'Sub now')]")
            )
        )
            print("🔒 Video requires subscription to watch. Taking screenshot of the page")
            self.capture_screenshot(request)

        except TimeoutException:
        #No subscription message found, try to find video element and take screenshot
            try:
                video_element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
                print("✅ Video is playing. Capturing screenshot.")
                self.capture_screenshot(request)

            except TimeoutException:
                print("Video element not found. Stream might not be live or available.")

    
       
        
        
        