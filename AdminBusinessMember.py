import time

from selenium.webdriver.common.by import By

from utilities.base_class import BaseFunc
from utilities.readProperties import ReadConfig
from pageObject.LoginPage import LoginUSHJA


class adminmember(BaseFunc):
        Name="ORGBUSINESS"
        link_organization_xpath="//ul[@class='MuiList-root MuiList-padding']//child::li[4]//child::button[@type='button']"
        textbox_search_xpath="//*[@type='text' and  @placeholder='Search member']"
        button_search_xpath="//*[@type='button' and  @class='MuiButtonBase-root MuiButton-root MuiButton-contained main-button MuiButton-containedPrimary'  ]//child::span[contains(text(),'Search')]"
        #link_orgname_xpath="//table[@class='MuiTable-root makeStyles-table-369']//child::th[text()='" + Name + "')]"

        text_businessmembership_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10']//child::h6[contains(text(),'Business Membership')]"
        text_membershiphistory_xpath = "//div[@class='MuiTableContainer-root']//descendant::*[contains(text(),'Business Membership')]"
        text_membership_click="//*[contains(text(),'Membership History')]//following::*[@class='MuiButtonBase-root MuiIconButton-root MuiAccordionSummary-expandIcon MuiIconButton-edgeEnd']"

        def __init__(self, driver):

            self.driver = driver
            self.baseURL = ReadConfig.getApplicationURL()
            self.username = ReadConfig.getUseremail()
            self.password = ReadConfig.getPassword()

        def adminorganisation(self,lusername):
            self.username1= lusername.upper()

            self.wait_presence_of_element_located(By.XPATH, self.link_organization_xpath).click()
            print("Username from config in upper:",self.username1)
            self.wait_presence_of_element_located(By.XPATH, self.textbox_search_xpath).send_keys(self.username1)
            time.sleep(2)
            self.wait_presence_of_element_located(By.XPATH, self.button_search_xpath).click()
            time.sleep(4)

            self.wait_presence_of_element_located(By.XPATH,"//table[contains(@class,'MuiTable-root makeStyles-table-')]//child::th[text()='" + self.username1 + "']").click()
            time.sleep(40)
            #self.driver.refresh()
            #time.sleep(20)

            business_org=self.wait_presence_of_element_located(By.XPATH,self.text_businessmembership_xpath)
            self.business_membership=business_org.text
            print("business membership:",self.business_membership)
            time.sleep(2)
            if(self.business_membership is None):
                assert False

            self.wait_presence_of_element_located(By.XPATH,self.text_membership_click).click()
            time.sleep(2)

            business_membership_history=self.wait_presence_of_element_located(By.XPATH,self.text_membershiphistory_xpath)
            print("business_membership_history:",business_membership_history.text)
            self.business_membership_history=business_membership_history.text
            if(self.business_membership_history == "Business Membership"):
                assert True
            else:
                assert False
            time.sleep(2)
        def adminbusinessmember(business,date):


            print(business)
