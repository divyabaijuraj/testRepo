import time

import pytest
import softest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ddt import ddt, data, unpack

from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminViewAfforgPrg import AdminViewAffOrgProgram
from utilities.customeLogger import LogGen
from utilities.utils import Utilities

@ddt
class TestAffiliateOrganization(softest.TestCase):
                logger = LogGen.loggen()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                @pytest.fixture(autouse=True)
                def class_setup(self):

                    self.admin =  LoginAdminUSHJA(self.driver)
                    self.adminview  =  AdminViewAffOrgProgram(self.driver)
                    self.logger = LogGen.loggen()

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "loginadmin"))
                @unpack
                def test_adminviewafforg(self,username,password,login_url,member_username):
                    self.admin.login_page_credentials(username,password,login_url)
                    time.sleep(7)
                    self.adminview.ViewAffOrg(member_username)
                    if(self.adminview.affname is None):
                        assert False
                        self.logger.info("View Dashboard doesnt contain Affiliate Name")
                    else:
                        assert True