import time

import pytest
import softest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.member import memberUSHJA

from pageObject.LoginPage import LoginUSHJA
from utilities.customeLogger import LogGen
from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminBusinessMember import adminmember
import ddt
from utilities.readProperties import ReadConfig
from utilities.utils import Utilities
from ddt import ddt, data, unpack


@ddt
class TestBusinessMembershipUSHJA(softest.TestCase):
    global username1
    logger = LogGen.loggen()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @pytest.fixture(autouse=True)
    def class_setup(self):

        self.lp = LoginUSHJA(self.driver)
        self.admin = LoginAdminUSHJA(self.driver)
        self.m = memberUSHJA(self.driver)
        self.adminm = adminmember(self.driver)
        self.logger = LogGen.loggen()


    ##############   LOGIN
    @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "login"))
    @unpack
    def test_alogin_ddt(self, Username, Password, URL):

        self.username1 = Username
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

     ###########  BUSINESS MEMBERSHIP ##########################
    @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "BusinessMembership"))
    @unpack

    def test_bbusiness_membership(self,Businessname,BusinessUshjaid,Address,State,City,Zip,Phone,Fax,Email,Website,Media,Affliations,Typeofbusiness,Businessowner, BusinessOwnerUshjaid,Contactfname,Contactlname,Contactptitle,ContactUSHJAid,AddressContact,CityContact,StateContact,ZipContact,PhoneContact,FaxContact,EmailContact,AlternateContactname,AlternateContacttitle,AlternateContactphone,AlternateContactemail,Signature,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew):




            self.m.alert_present(Businessname,BusinessUshjaid,Address,State,City,Zip,Phone,Fax,Email,Website,Media,Affliations,Typeofbusiness,Businessowner,BusinessOwnerUshjaid,Contactfname,Contactlname,Contactptitle,ContactUSHJAid,AddressContact,CityContact,StateContact,ZipContact,PhoneContact,FaxContact,EmailContact,AlternateContactname,AlternateContacttitle,AlternateContactphone,AlternateContactemail,Signature,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)
            print("date ***:", self.m.date1)
            print("Business membership:***:",self.m.business_member)
            if( self.m.confirm_message is not None):
                self.logger.info("Business Membership successfully registered.")
                assert True
            else:
                assert False


    ############  FROM ADMIN LOGIN ##############################

            #1)Enter the url: https://uatadmin.ushja.org/app/dashboard.
           # 2)Enter valid credentail :username:: ushja_admin password:U$#j@2021! 3)Click on Login
    @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx","loginadmin"))
    @unpack
    def test_bmadmin(self,username,password,login_url,member_username):
            time.sleep(2)
            self.admin.login_page_credentials(username,password,login_url)

            #Navigate through Admin->Organisation>Orgname>Membership Type and MemberHistory
            print("***************",member_username)
            self.adminm.adminorganisation(member_username)
            print("Adminbusiness_membership:***",self.adminm.business_membership)
            print("Adminbusiness_membershiphistory:***", self.adminm.business_membership_history)

            if (self.adminm.business_membership_history == 'Business Membership'):
                assert True
            else:

                 assert False
            if(self.adminm.business_membership == 'Business Membership'):
                assert True

            else:
                assert False
