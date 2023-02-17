import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.base_class import BaseFunc
class SignUp(BaseFunc):
    button_signup_xpath="//button[@class='signup-btn btn btn-secondary']"
    radio_orgaccount_type="//input[@id='accountType_2']"
    radio_indaccount_type="//input[@id='accountType_1']"
    textbox_username_xpath="//*[@id='root']/div[2]/section[2]/div/form/fieldset[1]/div[1]/div/input"
    textbox_password_xpath="//*[@id='root']/div[2]/section[2]/div/form/fieldset[1]/div[2]/div/input"
    textbox_confirmpassword_xpath="//input[@id='formConfirmPasseword']"
    #dropdown_select_title="//select[@id='formTitle']"
    #textbox_firstname_xpath= "//input[@id='formFirstName']"
   # textbox_middlename_xpath="//input[@id='formMiddleName']"
   # textbox_lastname_xpath="//input[@id='formLastName']"
    #textbox_suffix_xpath="//input[@id='formSuffix']"
    textbox_orgname_xpath="//input[@id='formOrganizationName']"
    #textbox_dob_xpath="//input[@id='formDOB']"
    textbox_address1_xpath="//input[@id='formAddress1']"
    textbox_address2_xpath="//input[@id='formAddress2']"
    textbox_city_xpath="//input[@id='formCity']"
    textbox_country_xpath="//select[@id='formCountry']"
    textbox_state_xpath="//input[@id='formState']"
    textbox_zip_xpath= "//input[@id='formZip']"
    dropdown_phone_xpath="//div[@class=' flag-dropdown']"
    textbox_dayphone_xpath="//input[@name='formPhone']"
    input_email_xpath="//input[@type='email']"
    button_submit_xpath="//button[@type='submit']"
    button_skip_xpath="//button[@type='button'  ]//child::span[contains(text(),'Skip')]"


    def sign_up(self,URL,AccountType,Username,Password,ConfirmPassword,OrganizationName,Address1,Address2,City,Country,State,Zip,PhoneCountry,Phone,Email):
        print("OK")
        time.sleep(2)
        self.driver.get(URL)
        time.sleep(4)
        self.wait_presence_of_element_located(By.XPATH,self.button_signup_xpath).click()
        if(AccountType=='Organization'):

           self.wait_presence_of_element_located(By.XPATH, self.radio_orgaccount_type).click()
           self.wait_presence_of_element_located(By.XPATH, self.textbox_username_xpath).send_keys(Username)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_password_xpath).send_keys(Password)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_confirmpassword_xpath).send_keys(ConfirmPassword)
           self.wait_presence_of_element_located(By.XPATH,self. textbox_orgname_xpath).send_keys(OrganizationName)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_address1_xpath).send_keys(Address1)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_address2_xpath).send_keys(Address2)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_city_xpath).send_keys(City)
           time.sleep(2)
           #select = self.wait_presence_of_element_located (By.XPATH,self.textbox_country_xpath ).click()
           select=Select(self.driver.find_element(By.XPATH,"//select[@id='formCountry']"))
           time.sleep(2)
           select.select_by_visible_text(Country)
           time.sleep(4)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_state_xpath).send_keys(State)
           time.sleep(2)
           self.wait_presence_of_element_located(By.XPATH, self.textbox_zip_xpath).send_keys(Zip)
           time.sleep(2)
           self.wait_presence_of_element_located(By.XPATH,self.dropdown_phone_xpath).click()
           time.sleep(10)
           self.wait_presence_of_element_located(By.XPATH,"//li/span[@class='country-name'  and contains(text(),'" + PhoneCountry  + "')]").click()
           time.sleep(2)
           self.wait_presence_of_element_located(By.XPATH,self.textbox_dayphone_xpath).send_keys(Phone)
           time.sleep(2)
           self.wait_presence_of_element_located(By.XPATH, self.input_email_xpath).send_keys(Email)
           time.sleep(2)
           self.wait_presence_of_element_located(By.XPATH, self.button_submit_xpath).click()
           time.sleep(4)
           self.wait_presence_of_element_located(By.XPATH,self.button_skip_xpath).click()
           time.sleep(2)




