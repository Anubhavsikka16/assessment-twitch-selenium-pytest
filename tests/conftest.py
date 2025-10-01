
import allure
import pytest
from allure_commons.types import AttachmentType
from utilities.configreader import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    
    outcome=yield
    rep=outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
# Fixture to log failure details and capture a screenshot if a test fails.
def log_on_failure(request, get_browser):
    yield
    item = request.node 
    driver = get_browser 
    
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name, attachment_type=AttachmentType.PNG)
        
        
        
@pytest.fixture(scope="function")
def get_browser(request):
    
    mobile_emulation = { "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3.0 } }

    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/140.0.0.0 Safari/537.36"
)

    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(10)

    request.cls.driver = driver
    
    
    driver.get(readConfig("basic info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
