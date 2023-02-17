import softest

from ddt import ddt, data, unpack
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.Learner import Learner
from pageObject.LoginPage1 import LoginiBridge360
from utilities.customeLogger import LogGen
from utilities.utils import Utilities






class TestLoginiBridge(softest.TestCase):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://learner.ibridge360.com/")
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utilities()
        self.lp=LoginiBridge360(self.driver)
        self.learner=Learner(self.driver)
        

    ##############  Login

    #@data(*Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\iBridge360\\TestData\\login_ibridge.xlsx","login"))

    #@unpack
    def test_login_ddt(self):
        username="ibridge@gmail.com"
        password="Ibridge@2021"
        #URL="https://learner.ibridge360.com/"
        logger = LogGen.loggen()
        print(username, password)
        self.obj=self.lp.login_iBridge(username, password)
        print(self.obj,"in test page")
        # if(self.driver.title == 'IBridge360'):
        #
        #
        #      logger.info("Logged in to IBridge360")
        #      print("Logged in ","^^^^^^^^^^^^^^^^")
        #
        #
        # else:
        #      logger.info("Error occured")
        #
        #

    # def test_learner(self):
    #     print("TITLE OF THE PAGE **************",self.driver.title)
    #     self.learner.dashboard_click()




