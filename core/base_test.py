import pytest

@pytest.mark.usefixtures("log_on_failure","get_browser")
class BaseTest:
    def __int__(self, driver):
        self.driver=driver