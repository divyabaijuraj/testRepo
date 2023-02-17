import softest

from ddt import ddt, data, unpack
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.Learner import Learner
from pageObject.member import memberUSHJA
from utilities.customeLogger import LogGen
from utilities.utils import Utilities


class TestLoginiBridge(softest.TestCase):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://uat.ushja.org/")

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utilities()
        self.lp = LoginiBridge360(self.driver)
        self.learner = Learner(self.driver)
