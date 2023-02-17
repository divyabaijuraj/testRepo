from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from utilities.customeLogger import LogGen


from string import ascii_letters

from utilities.base_class import BaseFunc
import time




class AdminViewAffOrgProgram(BaseFunc):
    global affname
    logger= LogGen.loggen()
    button_programs_xpath  =  "//ul[@class='MuiList-root MuiList-padding']//child::li[8]//child::button[@type='button']//child::span[@class='MuiButton-label']"
    link_USHJAAffiliateOrganizationMembers_xpath  =  "//table[contains(@class,'MuiTable-root makeStyles-table-')]//child::tr/td[contains(text(),'USHJA Affiliate Organization Members')]"
    input_searchorg_xpath="//input[@placeholder='Search Organization']"
    button_search_xpath="//span[contains(text(),'Search')]//parent::button"
    text_orgname_xpath="//*[text()='ORGTESTA4']"
    #arrow_orgname_xpath="//th[text()='ORGTESTA1']//parent::tr/td[1]/button"
    button_viewdashboard_xpath="//table/tbody/tr/td[5]/button[2]"

    textbox_affiliateName_name =  "affiliateName"

    def ViewAffOrg(self,member_username):

        self.wait_presence_of_element_located(By.XPATH, self.button_programs_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self.link_USHJAAffiliateOrganizationMembers_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self.input_searchorg_xpath).send_keys(member_username)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self.button_search_xpath).click()
        time.sleep(4)

        organization_name= self.wait_presence_of_element_located(By.XPATH, "//*[text()='" + member_username.upper() + "']")
        print("Organization_name ",organization_name.text)
        time.sleep(4)
        if(organization_name.text is None):
                        assert False
                        self.logger.info("Organization name not exists")
                        self.driver.close()
        else:
                        self.wait_presence_of_element_located(By.XPATH, "//th[text()='" + member_username.upper() + "']//parent::tr/td[1]/button").click()
                        time.sleep(2)




        self.wait_presence_of_element_located(By.XPATH,self.button_viewdashboard_xpath).click()
        time.sleep(3)
        affiliate_name =  self.wait_presence_of_element_located(By.NAME,self.textbox_affiliateName_name)
        print("Attribute value:",affiliate_name.get_attribute('value'))
        self.affname=affiliate_name.get_attribute('value')
        time.sleep(3)
