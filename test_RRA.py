import time
import pytest
import softest

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.member import memberUSHJA
from pageObject.LoginPage import LoginUSHJA
from utilities.customeLogger import LogGen
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.RRA import RecognizedRdingAcademy
from utilities.readProperties import ReadConfig
from utilities.utils import Utilities

@ddt
class TestLoginUSHJA(softest.TestCase):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @pytest.fixture(autouse=True)
    def class_setup(self):

        self.lp = LoginUSHJA(self.driver)
        self.admin= LoginAdminUSHJA(self.driver)
        self.rra = RecognizedRdingAcademy(self.driver)
        self.logger = LogGen.loggen()
    #
    # def  test_alogin(self):
    #     ###  1)Enter the url https://uat.ushja.org/
    #     ##   2) Enter valid credential
    #     #    3)Click on login.
    #     self.lp.login_page_credentials()
    #     ushja_title="USHJA"
    #     ##Verify Login page
    #     self.logger.info("Verifying Login Page")
    #     if ushja_title == "USHJA":
    #         print("from login page title")
    #         assert True
    #
    #         self.logger.info("***** USHJA Home page title test is passed *********")
    #         time.sleep(2)
    #
    #
    #     else:
    #         self.driver.save_screenshot(".\\Screenshot\\" + "test_USHJAhomepageTitle.png")
    #         self.logger.error("*****USHJA Home page title test is failed *********")
    #         self.driver.close()
    #         assert False
    #
        ##############   LOGIN
    @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx","login"))
    @unpack
    def test_alogin_ddt(self, Username, Password, URL):
            ###  1)Enter the url https://uat.ushja.org/
            #     ##   2) Enter valid credential
            #     #    3)Click on login.

            logger = LogGen.loggen()
            print(Username, Password)
            self.lp.login_page_credentials(Username, Password, URL)
            ushja_title = "USHJA"
            ##Verify Login page
            self.logger.info("Verifying Login Page")
            if ushja_title == "USHJA":
                print("from login page title")
                assert True

                self.logger.info("***** USHJA Home page title test is passed *********")
                time.sleep(10)


            else:
                self.driver.save_screenshot(".\\Screenshot\\" + "test_USHJAhomepageTitle.png")
                self.logger.error("*****USHJA Home page title test is failed *********")
                self.driver.close()
                assert False

        ##4)ORG>MYPROGRAMS>USHJA Recognized Riding Academy>Enroll

            self.rra.alertRRA_present()