import time

import pytest
import softest


from pageObject.member import memberUSHJA

from pageObject.LoginPage import LoginUSHJA
from utilities.customeLogger import LogGen
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminBusinessMember import adminmember

from utilities.readProperties import ReadConfig
from utilities.utils import Utilities


class TestLoginUSHJA(softest.TestCase):

    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.lp = LoginUSHJA(self.driver)
        self.admin= LoginAdminUSHJA(self.driver)
        self.m = memberUSHJA(self.driver)
        self.adminm = adminmember(self.driver)
        self.logger = LogGen.loggen()


    def  test_alogin(self):
        ###  1)Enter the url https://uat.ushja.org/
        ##   2) Enter valid credential
        #    3)Click on login.
        self.lp.login_page_credentials()
        ushja_title="USHJA"
        ##Verify Login page
        self.logger.info("Verifying Login Page")
        if ushja_title == "USHJA":
            print("from login page title")
            assert True

            self.logger.info("***** USHJA Home page title test is passed *********")
            time.sleep(2)


        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_USHJAhomepageTitle.png")
            self.logger.error("*****USHJA Home page title test is failed *********")
            self.driver.close()
            assert False


        ##4)Click on Quick Actions>Business membership
        # 6)2023 Business membership form
        # 7) Business information  Form,Primary Business Contact Information,Signature of primary business contact
        # Making payment and Order Confirmation fill these and submit form
        self.m.alert_present()
        # print("date ***:",self.m.date1)
        # print("Business membership:***:",self.m.business_member)


        #1)Enter the url: https://uatadmin.ushja.org/app/dashboard. 2)Enter valid credentail :username:: ushja_admin password:U$#j@2021! 3)Click on Login
        # self.admin.login_page_credentials()
        #
        # #Navigate through Admin->Organisation>Orgname>Membership Type and MemberHistory
        # self.adminm.adminorganisation()
        # print("business_membership:***",self.adminm.business_membership)
        # print("business_membershiphistory:***", self.adminm.business_membership_history)
        # # #self.a.affiliate_Organisation()
        # if (self.driver.title == 'USHJA'):
        #     print("OK")
        #
        # if(self.m.business_member == self.adminm.business_membership):
        #     assert True
        #
        # else:
        #     assert False
    # def test_business_membership(self):
    #    # self.lp.login_page_credentials(self.username, self.password)
    #     time.sleep(6)
    #     self.m.alert_present()

    # def test_affiliate_organisation(self):
    #     self.lp.login_page_credentials(self.username, self.password)
    #     time.sleep(6)
    #     self.a.affiliate_Organisation()

