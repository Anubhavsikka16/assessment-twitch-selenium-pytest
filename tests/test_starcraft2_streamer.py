
import pytest
from business_pages.home_page import HomePage
from business_pages.home_page import StreamerPage
from core.base_test import BaseTest
import time

class TestTwitchStarcraftFlowMobile(BaseTest):
    
    @pytest.mark.assessment
    def test_twitch_starcraft_flow_mobile(self, request):
        home = HomePage(self.driver)
        # 2. click search
        home.click_search()
        # 3. input "StarCraft II"
        results=home.enter_text("StarCraft II")
        time.sleep(5)
        #4. Scrool down the page to load more videos
        results.scroll_down_times()
        #5. Click on one streamer
        results.click_one_streamer()
        #6. Take a screenshot of the video streamer
        results.check_for_modal(request)