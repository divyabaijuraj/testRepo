import time

import pytest
import softest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ddt import ddt, data, unpack

from pageObject.LoginAdmin import LoginAdminUSHJA
from pageObject.AdminAddenrollmentAffOrgProg import AdminAddEnrollmentAffOrgProgms
from pageObject.AffiliateOrganisation import AffiliateOrganisation
from utilities.customeLogger import LogGen
from utilities.utils import Utilities

@ddt
class TestAffiliateOrganization(softest.TestCase):
                logger = LogGen.loggen()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

                @pytest.fixture(autouse=True)
                def class_setup(self):

                    self.admin =  LoginAdminUSHJA(self.driver)
                    self.adminEnroll = AdminAddEnrollmentAffOrgProgms(self.driver)
                    self.afforg= AffiliateOrganisation(self.driver)
                    self.logger = LogGen.loggen()

                @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "AdminAffOrgAddenroll"))
                @unpack
                def test_Adminaddenrollment(self,username,password,login_url,member_username,AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,Otherpgm,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile):

                    self.admin.login_page_credentials(username,password,login_url)
                    time.sleep(2)
                    self.adminEnroll.addenrollment(member_username)
                    time.sleep(2)
                    self.afforg.affiliate_Organisation(AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile)
                    time.sleep(2)
                    self.adminEnroll.enrollment_submit()