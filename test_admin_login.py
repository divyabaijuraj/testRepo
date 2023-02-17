import time

import pytest
import softest

from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObject.member import memberUSHJA
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminBusinessMember import adminmember
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig

class TestAdminLoginUSHJA(softest.TestCase):
    # baseURL = ReadConfig.getadminURL()
    # username = ReadConfig.getAdminUser()
    # password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup

        self.lp = LoginAdminUSHJA(self.driver)
        self.m = adminmember(self.driver)
        #self.ut = Utilities()

    # def test_alogin(self):
    #         self.lp.login_page_credentials(self.username, self.password)
    #         if (self.driver.title == 'USHJA'):
    #             print("OK")
    #
    #         time.sleep(2)
    #         self.driver.close()
    def  test_admin_businessmember(self):
        self.lp.login_page_credentials()
        self.m.adminorganisation()