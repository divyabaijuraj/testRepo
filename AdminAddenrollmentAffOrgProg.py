from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from utilities.customeLogger import LogGen

from string import ascii_letters

from utilities.base_class import BaseFunc
import time


class AdminAddEnrollmentAffOrgProgms(BaseFunc):
    logger = LogGen.loggen()
    button_programs_xpath = "//ul[@class='MuiList-root MuiList-padding']//child::li[8]//child::button[@type='button']//child::span[@class='MuiButton-label']"
    link_USHJAAffiliateOrganizationMembers_xpath = "//table[contains(@class,'MuiTable-root makeStyles-table-')]//child::tr/td[contains(text(),'USHJA Affiliate Organization Members')]"
    button_Add_Enrollment_xpath="//span[contains(text(),'Add Enrollment')]//parent::button"
    dropdown_organization_name="orgName"
    textbox_startdate_xpath="//div[@class='MuiFormControl-root MuiTextField-root MuiFormControl-fullWidth' ]//child::label[contains(text(),'Start ')]//parent::div//child::div[1]/input"
    textbox_paiddate_xpath = "//div[@class='MuiFormControl-root MuiTextField-root MuiFormControl-fullWidth' ]//child::label[contains(text(),'Paid ')]//parent::div//child::div[1]/input"
    button_continue_xpath = "//span[contains(text(),'Continue')]//parent::button"
    button_submit_xpath="//span[contains(text(),'Submit')]//parent::button"
    def addenrollment(self,member_username):
        self.wait_presence_of_element_located(By.XPATH, self.button_programs_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.link_USHJAAffiliateOrganizationMembers_xpath).click()
        time.sleep(4)
        self.wait_presence_of_element_located(By.XPATH,self.button_Add_Enrollment_xpath).click()
        time.sleep(3)
        #self.wait_presence_of_element_located(By.NAME,self.dropdown_organization_name).send_keys("orgtesta3")
        organization=self.wait_presence_of_element_located(By.NAME,self.dropdown_organization_name)
        organization.send_keys(member_username)
        time.sleep(5)
        print("ORGVALUE",organization.get_attribute('value'))
        if (organization.get_attribute('value') is not None):
             organization.send_keys(Keys.DOWN)
             time.sleep(4)
             organization.send_keys(Keys.ENTER)
             time.sleep(2)
             organization.send_keys(Keys.TAB)
        time.sleep(2)


        # arrow_button =self.wait_presence_of_element_located(By.XPATH,"//*[@id='root']/div[1]/header/div[2]/div[1]/form/div/div/div/div/button[2]")
        # self.driver.execute_script("arguments[0].click();", arrow_button)
        # time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self.textbox_startdate_xpath).send_keys("12/12/2000")
        time.sleep(4)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_paiddate_xpath).send_keys("12/12/2000")
        time.sleep(4)
        self.wait_presence_of_element_located(By.XPATH,self.button_continue_xpath).click()
        time.sleep(2)

    def enrollment_submit(self):
        self.wait_presence_of_element_located(By.XPATH,self.button_submit_xpath).click()
        time.sleep(2)
