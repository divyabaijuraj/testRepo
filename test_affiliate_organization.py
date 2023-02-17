import time

import pytest
import softest
from pageObject.AffiliateOrganisation import AffiliateOrganisation
from pageObject.LoginPage import LoginUSHJA
from utilities.customeLogger import LogGen
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminAffiliateOrganisation import AdminAffiliateOrg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ddt import ddt, data, unpack

from utilities.utils import Utilities


# class TestAffiliateOrganization(softest.TestCase):
#
#     logger = LogGen.loggen()
#
#     @pytest.fixture(autouse=True)
#     def class_setup(self, setup):
#         self.driver = setup
#         self.lp = LoginUSHJA(self.driver)
#         self.admin= LoginAdminUSHJA(self.driver)
#         self.org= AffiliateOrganisation(self.driver)
#         self.adminorg=AdminAffiliateOrg(self.driver)
#
#     def test_affiliateorg(self):
#             ###  1)Enter the url https://uat.ushja.org/
#             ##   2) Enter valid credential
#             #    3)Click on login.
#             self.lp.login_page_credentials()
#             ##4)Click on Quick Actions>Affiliate Organization
#             # 6)Affiliate Information Form
#             # 7th step
#             # 1)Organization Information   Form,2)Affiliate contact person  Information,3)Signature
#             # #####  4)Committee Representation Criteria 5)Organization Information Survey6)Making payment and7) Order Confirmation fill these and submit form
#             #Form submission
#
#             self.org.alertorg_present()
#
#             # Message check after successful submission of the form
#             print("After submission message shown from member:",self.org.aff_confirmation)
#
#             # status check after submission in enclose button of affiliate org
#             print("After submission enclose button from member:",self.org.affiliateorg)
#
#             # check date in enclose button of affiliate org
#             print("Affiliate date from member Enclose button:",self.org.aff_date)

@ddt
class TestAffiliateOrganization(softest.TestCase):
                logger = LogGen.loggen()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                @pytest.fixture(autouse=True)
                def class_setup(self):
                    self.lp = LoginUSHJA(self.driver)
                    self.admin = LoginAdminUSHJA(self.driver)

                    self.org = AffiliateOrganisation(self.driver)
                    self.adminorg = AdminAffiliateOrg(self.driver)
                    self.logger = LogGen.loggen()

            ##############   LOGIN

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "login"))
                @unpack
                def test_alogin_ddt(self, Username, Password, URL):
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
                        ##4)Click on Quick Actions>Affiliate Organization
                        #             # 6)Affiliate Information Form
                        #             # 7th step
                        #             # 1)Organization Information   Form,2)Affiliate contact person  Information,3)Signature
                        #             # #####  4)Committee Representation Criteria 5)Organization Information Survey6)Making payment and7) Order Confirmation fill these and submit form
                        #             #Form submission
                        #

                        else:
                            self.driver.save_screenshot(".\\Screenshot\\" + "test_USHJAhomepageTitle.png")
                            self.logger.error("*****USHJA Home page title test is failed *********")
                            self.driver.close()
                            assert False

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx","AffiliateOrg"))
                @unpack
                def test_org_affiliate(self,AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID):
                             self.org.alertorg_present(AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID)



