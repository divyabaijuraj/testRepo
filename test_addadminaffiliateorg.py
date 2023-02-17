import time

import pytest
import softest


from utilities.customeLogger import LogGen
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminAddAffiliateOrganization import AdminAddAffiliateOrganization
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ddt import ddt, data, unpack

from utilities.utils import Utilities

@ddt
class TestAffiliateOrganization(softest.TestCase):
                logger = LogGen.loggen()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                @pytest.fixture(autouse=True)
                def class_setup(self):

                    self.admin =  LoginAdminUSHJA(self.driver)
                    self.adminaddOrg  =  AdminAddAffiliateOrganization(self.driver)


                    self.logger = LogGen.loggen()

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "Adminaddorg"))
                @unpack
                def test_adminaddorg_ddt(self,AdminURL,AdminUsername,AdminPassword,OrganizationName,Address1,Address2,City,State,Zip,Country,PhoneCountry,Phone,Email):

                    self.admin.login_page_credentials(AdminUsername,AdminPassword,AdminURL)
                    time.sleep(2)
                    ushja_title='USHJA Admin'
                    if ushja_title == "USHJA Admin":
                        print("from login page title")
                        assert True

                        self.logger.info("***** USHJA Home page title test is passed *********")
                        time.sleep(10)



                    else:
                        self.driver.save_screenshot(".\\Screenshot\\" + "test_USHJAhomepageTitle.png")
                        self.logger.error("*****USHJA Home page title test is failed *********")
                        self.driver.close()
                        assert False

                    self.adminaddOrg.addadminafforg(OrganizationName,Address1,Address2,City,State,Zip,Country,PhoneCountry,Phone,Email)





