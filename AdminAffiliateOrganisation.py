import time

from selenium.webdriver.common.by import By

from utilities.base_class import BaseFunc
from utilities.readProperties import ReadConfig


class AdminAffiliateOrg(BaseFunc):

        link_organization_xpath="//ul[@class='MuiList-root MuiList-padding']//child::li[4]//child::button[@type='button']"
        textbox_search_xpath="//*[@type='text' and  @placeholder='Search member'  ]"
        button_search_xpath="//*[@type='button' and  @class='MuiButtonBase-root MuiButton-root MuiButton-contained main-button MuiButton-containedPrimary'  ]//child::span[contains(text(),'Search')]"
        link_orgname_xpath="//*[@id='enhanced-table-checkbox-0'  and @scope='row']"

        text_affiliate_org_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10']//child::h6[contains(text(),'Affiliate Organization')]"
        text_membershiphistory_xpath = "//div[@class='MuiTableContainer-root']//descendant::*[contains(text(),'Affiliate Organization')]"
        text_membership_click="//*[contains(text(),'Membership History')]//following::*[@class='MuiButtonBase-root MuiIconButton-root MuiAccordionSummary-expandIcon MuiIconButton-edgeEnd']"

        def __init__(self, driver):

            self.driver = driver
            self.baseURL = ReadConfig.getApplicationURL()
            self.username = ReadConfig.getUseremail()
            self.password = ReadConfig.getPassword()

        def adminorganisation(self,lusername):
            self.username1=lusername.upper()
            self.wait_presence_of_element_located(By.XPATH, self.link_organization_xpath).click()
            print("Username from config:",self.username)
            self.wait_presence_of_element_located(By.XPATH, self.textbox_search_xpath).send_keys(self.username1)
            time.sleep(2)
            self.wait_presence_of_element_located(By.XPATH, self.button_search_xpath).click()
            time.sleep(2)
            self.wait_presence_of_element_located(By.XPATH,self.link_orgname_xpath).click()
            time.sleep(10)

            affiliate_org=self.wait_presence_of_element_located(By.XPATH,self.text_affiliate_org_xpath)
            self.affiliate_org=affiliate_org.text
            print("Affiliate membership:",self.affiliate_org)
            time.sleep(15)
            if(self.affiliate_org is None):
                assert False

            self.wait_presence_of_element_located(By.XPATH,self.text_membership_click).click()
            time.sleep(2)

            affiliate_org_history=self.wait_presence_of_element_located(By.XPATH,self.text_membershiphistory_xpath)
            print("Affiliate_membership_history:",affiliate_org_history.text)
            self.affiliate_org_history=affiliate_org_history.text
            if(self.affiliate_org_history == "Affiliate Organization"):
                assert True
            else:
                assert False
                time.sleep(2)
