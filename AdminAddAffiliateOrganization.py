from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from detect_delimiter import detect
from string import ascii_letters

from utilities.base_class import BaseFunc
import time

class AdminAddAffiliateOrganization(BaseFunc):

    link_organization_xpath = "//ul[@class='MuiList-root MuiList-padding']//child::li[4]//child::button[@type='button']"
    button_addorganization_xpath="//button[@type='button']//child::span[contains(text(),'Add Organization')]"
    input_organizationname_xpath="//input[@id='organizationName']"
    input_address1_xpath = "//input[@id='address1']"
    input_address2_xpath = "//input[@id='address2']"
    input_city_xpath="//input[@id='city']"
    dropdown_state_xpath="//div[@id='state']"
    input_zip_xpath="//input[@id='zip']"
    dropdown_country_xpath="//div[@id='country']"

    dropdown_phone_xpath="//div[@class='arrow']"

    input_phone_name="formPhone"
    input_email_xpath="//input[@id='email']"

    def addadminafforg(self,OrganizationName,Address1,Address2,City,State,Zip,Country,PhoneCountry,Phone,Email):


        self.wait_presence_of_element_located(By.XPATH, self.link_organization_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.button_addorganization_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.input_organizationname_xpath).send_keys(OrganizationName)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.input_address1_xpath).send_keys(Address1)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.input_address2_xpath).send_keys(Address2)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.input_city_xpath).send_keys(City)

        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.dropdown_state_xpath).click()
        time.sleep(2)
        print("STATE GIVEN:",State)
        print("State in upper:",State.upper())

        self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + State + "')]").click()
        time.sleep(5)
        self.wait_presence_of_element_located(By.XPATH, self.input_zip_xpath).send_keys(Zip)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self.dropdown_country_xpath).click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + Country.upper() + "')]").click()
        time.sleep(10)
        self.wait_presence_of_element_located(By.XPATH,self.dropdown_phone_xpath).click()
        time.sleep(10)
        self.wait_presence_of_element_located(By.XPATH," //ul[@class=' country-list']//child::li/span[contains(text(),'" + PhoneCountry.capitalize() + "')]").click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.NAME,self.input_phone_name).send_keys(Phone)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,self. input_email_xpath).send_keys(Email)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH,"//button[@type='button' and contains(text(),'Add Organization')]").click()
        time.sleep(2)


