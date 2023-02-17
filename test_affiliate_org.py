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

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "AffiliateOrg"))
                @unpack
                def test_alogin_ddt(self, Username, Password, URL,AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,Otherpgm,NeedsAffiliateOrg,EducationPrograms,EducationDescription
,AdditionalComments,ChooseFile,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew,AdminURL,AdminUsername,AdminPassword,lusername):




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

                        self.org.alertorg_present(AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription
,AdditionalComments,ChooseFile,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)

                        time.sleep(4)
                        print("Username:",Username)
                        self.lp.Logout()
                        time.sleep(4)
                        #########  Login to admin
                        ##1)Enter the url: https://uatadmin.ushja.org/app/dashboard.
                        # # 2)Enter valid credentail :username:: ushja_admin password:U$#j@2021!
                        # 3)Click on Login
                      #  self.admin.login_page_credentials(AdminUsername,AdminPassword,AdminURL)

                        # Navigate through Admin->Organisation>Orgname>Membership Type and MemberHistory
                       # self.adminorg.adminorganisation(lusername)



