import time

from utilities.customeLogger import LogGen
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.AdminBusinessMember import adminmember
from pageObject.Learner import Learner
from utilities.base_class import BaseFunc





class memberUSHJA(BaseFunc):
   global date1
   alert_xpath="//*[@id='react-joyride-step-0']/div/div/div/div[2]/div/button"
   text_alertskip_xpath = "//button[@title='Skip']"

   xpath_button_business="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12']//child::p[contains(text(),'Business Membership')]"

   business_business_xpath =   "//*[@id='root']/div[1]/div[2]/main/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/p"
   radio_comp_year="//span[@class='MuiIconButton-label']//child::input[@class='PrivateSwitchBase-input-244' or @type='radio']"
   button_continue_xpath="//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-text makeStyles-nextStep-231'  or @type='button']//child::span[contains(text(),'Continue')]"
   textbox_businessname_xpath="//input[@name='name'  and @class='MuiInputBase-input MuiInput-input']"
   textbox_ushaid_xapth="//input[@name='id']"
   textbox_address_xpath="//input[@name='address']"
   textbox_city_xpath="//input[@name='city']"
   textbox_state_xpath="//input[@name='state']"
   textbox_zip_xpath="//input[@name='zip']"
   textbox_phone_xpath="//input[@name='phone']"
   textbox_fax_xpath="//input[@name='fax']"
   textbox_email_xpath="//input[@name='email']"
   textbox_website_xpath="//input[@name='website']"
   textbox_facebook_name="socialMedia"
   dropdown_primarybusiness_xpath="//div[@id='mui-component-select-primaryBusiness']"
   textbox_businessowner_name="businessOwner"
   textbox_ushjaid_name="businessId"
   checkbox_affiliations_name="affliations"
   text_otherAffliations_name="otherAffliations"

  # button_continue2_xpath="/html/body/div[5]/div[3]/div/div[4]/div/div/button[2]/span[1]"
   button_continue2_xpath = "//*[@class ='MuiGrid-root MuiGrid-container MuiGrid-justify-xs-flex-end' or @style='opacity: 1;']//child::button/span[contains(text(),'Continue')]"
   ###Primary Business Contact Information

   textbox_contactfname_name="contactFirstName"
   textbox_contactlname_name="contactLastName"
   textbox_contactperson_name="contactPersonTitle"
   textbox_ushjaid2_name="contactUshjaId"
   textbox_address_xpath="//*[@name='address']"
   textbox_city_xpath="//*[@name='city']"
   dropdown_state_id="mui-component-select-state"
   textbox_zip_xpath="//*[@name='zip']"
   textbox_phone_xpath="//*[@name='phone']"
   textbox_fax_xpath="//*[@name='fax']"
   textbox_email_xpath="//*[@name='email']"
   textbox_alternatefname_name="alternateContactName"
   textbox_alternatectitle_name="alternateContactTitle"
   textbox_alternatephone_name = "alternateContactPhone"
   textbox_alternateemail_name = "alternateContactEmail"
   #button_businesscontact_continue="/html/body/div[5]/div[3]/div/div[4]/div/div/button[2]/span[1]"
   button_businesscontact_continue = "//*[@class ='MuiGrid-root MuiGrid-container MuiGrid-justify-xs-flex-end' or @style='opacity: 1;']//child::button/span[contains(text(),'Continue')]"


    #################Signature of primary business contact

   textbox_sign_xpath ="//input[@class='MuiInputBase-input MuiOutlinedInput-input']"
   button_signatureof_businesscontact_xpath="//*[@class ='MuiGrid-root MuiGrid-container MuiGrid-justify-xs-flex-end' or @style='opacity: 1;']//child::button/span[contains(text(),'Continue')]"

   #################Making payment
   text_your_saved_creditcards_xpath="//*[contains(text(),'Your saved credit cards')]"
   radio_your_saved_creditcards_xpath ="//div[@class='MuiBox-root MuiBox-root-361']//child::input[@class='PrivateSwitchBase-input-242']"
   textbox_firstname_name="firstName"
   textbox_lastname_name="lastName"
   textbox_address_name="line1"
   textbox_postalcode_name="postal_code"
   textbox_cardno_xpath="//input[@placeholder='Card number']"
   textbox_mmdd_xpath="// input[ @ id = 'card-expiry']"
   textbox_cvc_xpath="//input[@id='cvc']"
   checkbox_savecard_name="saveMyCard"
   checkbox_renewcard_name="autoRenewMembership"
   button_pay_xpath="//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-text makeStyles-nextStep-231'  or @type='button']//child::span[contains(text(),'Pay')]"


  ################### Order Confirmation

   text_orderconfirmation_xpath  = "//h4[contains(text(), 'Business Membership Application Successful')]"
   close_button_xpath="//*[@class='MuiButtonBase-root MuiIconButton-root'  and @aria-label='close']"
   text_aftersubmssion_xpath="//*[@id='root']/div[1]/div[2]/main/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/p"
   text_date_xpath="//*[@id='root']/div[1]/div[2]/main/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/p"

   ############### STATUS BAR
   text_status_business_membership_xpath="//p[contains(@class,'MuiTypography-root makeStyles-contactInfoDetails-') and (text()='Business Membership')]"

   def saved_credit_cards(self):
       self.wait_presence_of_element_located(By.XPATH, self.radio_your_saved_creditcards_xpath).click()
       time.sleep(2)

   def business_membership_click(self,Businessname,BusinessUshjaid,Address,State,City,Zip,Phone,Fax,Email,Website,Media,Affliations,Typeofbusiness,Businessowner, BusinessOwnerUshjaid,Contactfname,Contactlname,Contactptitle,ContactUSHJAid,AddressContact,CityContact,StateContact,ZipContact,PhoneContact,FaxContact,EmailContact,AlternateContactname,AlternateContacttitle,AlternateContactphone,AlternateContactemail,Signature,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew):


              #  time.sleep(2)
             # date_business_membershp=self.wait_presence_of_element_located(By.XPATH,self.text_date_xpath)
             # if(date_business_membershp.is_displayed()):
             #     quit()
             # else:
                 time.sleep(4)
                 self.wait_presence_of_element_located(By.XPATH,self.xpath_button_business).click()
                 time.sleep(2)

                 comp_year = self.wait_presence_of_element_located(By.XPATH,self.radio_comp_year)
                 if(comp_year.is_enabled()):

                       self.wait_presence_of_element_located(By.XPATH, self.radio_comp_year).click()

                 # time.sleep(2)
                 self.wait_presence_of_element_located(By.XPATH,self.button_continue_xpath).click()
                ##########   Business information  Form

                 time.sleep(2)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_businessname_xpath).send_keys(Businessname)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_ushaid_xapth).send_keys(BusinessUshjaid)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_address_xpath).send_keys(Address)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_state_xpath).send_keys(State)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_city_xpath).send_keys(City)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_zip_xpath).send_keys(Zip)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_phone_xpath).send_keys(Phone)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_fax_xpath).send_keys(Fax)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_email_xpath).send_keys(Email)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_website_xpath).send_keys(Website)
                 self.wait_presence_of_element_located(By.NAME, self.textbox_facebook_name).send_keys(Media)
                 checkbox_list = self.wait_presence_of_all_elements_located(By.NAME, self.checkbox_affiliations_name)
                 print(len(checkbox_list))
                 checkbox_list[Affliations].click()
                 if(Affliations ==6):
                       self.wait_presence_of_element_located(By.NAME,self.text_otherAffliations_name).send_keys("Other Affliations")

                 self.wait_presence_of_element_located(By.XPATH,self.dropdown_primarybusiness_xpath).click()
                 #click on any element

                 self.wait_presence_of_element_located(By.XPATH,"//li[contains(text(),'" + Typeofbusiness + "')]").click()

                 self.wait_presence_of_element_located(By.NAME,self.textbox_businessowner_name).send_keys(Businessowner)

                 self.wait_presence_of_element_located(By.NAME,self.textbox_ushjaid_name).send_keys(BusinessOwnerUshjaid)


                 self.wait_presence_of_element_located(By.XPATH,self.button_continue2_xpath).click()

                 time.sleep(2)

                 ###Primary Business Contact Information
                 self.wait_presence_of_element_located(By.NAME,self.textbox_contactfname_name).send_keys(Contactfname)
                 self.wait_presence_of_element_located(By.NAME,self.textbox_contactlname_name).send_keys(Contactlname)
                 self.wait_presence_of_element_located(By.NAME, self.textbox_contactperson_name).send_keys(Contactptitle)
                 self.wait_presence_of_element_located(By.NAME,self.textbox_ushjaid2_name).send_keys(ContactUSHJAid)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_address_xpath).send_keys(AddressContact)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_city_xpath).send_keys(CityContact)
                 self.wait_presence_of_element_located(By.ID,self.dropdown_state_id).click()

                 self.wait_presence_of_element_located(By.XPATH, "//li[contains(text(),'" + StateContact +  "')]").click()
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_zip_xpath).send_keys(ZipContact)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_phone_xpath).send_keys(PhoneContact)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_fax_xpath).send_keys(FaxContact)
                 self.wait_presence_of_element_located(By.XPATH,self.textbox_email_xpath).send_keys(EmailContact)
                 self.wait_presence_of_element_located(By.NAME,self.textbox_alternatefname_name).send_keys(AlternateContactname)
                 self.wait_presence_of_element_located(By.NAME,self.textbox_alternatectitle_name).send_keys(AlternateContacttitle)
                 self.wait_presence_of_element_located(By.NAME,self.textbox_alternatephone_name).send_keys(AlternateContactphone)

                 self.wait_presence_of_element_located(By.NAME,self.textbox_alternateemail_name).send_keys(AlternateContactemail)

                 self.wait_presence_of_element_located(By.XPATH,self.button_businesscontact_continue).click()
                 time.sleep(2)

   #               ########### Signature of primary business contact
   #
                 self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                 time.sleep(2)

                 self.wait_presence_of_element_located(By.XPATH,self.textbox_sign_xpath).send_keys(Signature)
                 time.sleep(2)
                 self.wait_presence_of_element_located(By.XPATH,self.button_signatureof_businesscontact_xpath).click()


                 ##############  Making payment

                 time.sleep(2)
                 if(self.wait_presence_of_element_located(By.XPATH, "//*[contains(text(),'Add Credit Card')]//preceding-sibling::span//child::span/input").is_selected()):
                    pass
                 else:
                    self.wait_presence_of_element_located(By.XPATH, "//*[contains(text(),'Add Credit Card')]//preceding-sibling::span//child::span/input").click()
                    time.sleep(2)


                 # try:
                 #
                 #     saved_credit_card = self.wait_presence_of_element_located(By.XPATH,self.text_your_saved_creditcards_xpath)
                 #     if (saved_credit_card.text == 'Your saved credit cards'):
                 #         self.saved_credit_cards()
                 # except Exception:
                 #     print("Element does not exist")

                 self.wait_presence_of_element_located(By.NAME, self.textbox_firstname_name).send_keys(creditcard_firstname)
                 self.wait_presence_of_element_located(By.NAME, self.textbox_lastname_name).send_keys(Creditcard_lastname)
                 self.wait_presence_of_element_located(By.NAME, self.textbox_address_name).send_keys(Creditcard_address)

                 self.wait_presence_of_element_located(By.NAME, self.textbox_postalcode_name).send_keys(Creditcard_postalcode)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_cardno_xpath).send_keys(Creditcard_cardno)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_mmdd_xpath).send_keys(Creditcard_mmyy)
                 self.wait_presence_of_element_located(By.XPATH, self.textbox_cvc_xpath).send_keys(Creditcard_cvc)
                 if(Savemycard.capitalize() =='Yes'):
                      self.wait_presence_of_element_located(By.NAME, self.checkbox_savecard_name).click()
                 else:
                    pass

                 if(Autorenew.capitalize() == 'Yes'):
                    self.wait_presence_of_element_located(By.NAME,self.checkbox_renewcard_name).click()
                 else:
                    pass


                 self.wait_presence_of_element_located(By.XPATH, self.button_pay_xpath).click()
                 time.sleep(2)





                 #######################  Order Confirmation
                 order_confirm=self.wait_presence_of_element_located(By.XPATH,self.text_orderconfirmation_xpath)
                 print(order_confirm.text)
                 self.confirm_message=order_confirm.text

                 time.sleep(2)
                 self.wait_presence_of_element_located(By.XPATH,self.close_button_xpath).click()

                 time.sleep(4)
                 business=self.wait_presence_of_element_located(By.XPATH,self.text_aftersubmssion_xpath)
                 self.business_member= business.text

                 print("business member:",self.business_member)
                 date=self.wait_presence_of_element_located(By.XPATH, self.text_date_xpath)
                 self.date1= date.text
                 print("date=",self.date1)
                 if(self.date1 is None):
                     assert False
                 else:
                     assert True


                 time.sleep(2)
                 status_business_membership = self.wait_presence_of_element_located(By.XPATH,self.text_status_business_membership_xpath)
                 print("status_business_membership***:",status_business_membership.text)
                 # time.sleep(4)



   def alert_present(self,Businessname,BusinessUshjaid,Address,State,City,Zip,Phone,Fax,Email,Website,Media,Affliations,Typeofbusiness,Businessowner, BusinessOwnerUshjaid,Contactfname,Contactlname,Contactptitle,ContactUSHJAid,AddressContact,CityContact,StateContact,ZipContact,PhoneContact,FaxContact,EmailContact,AlternateContactname,AlternateContacttitle,AlternateContactphone,AlternateContactemail,Signature,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew):

       try:

                self.wait_presence_of_element_located(By.XPATH, self.text_alertskip_xpath).click()
               # WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(By.XPATH, self.text_alertskip_xpath)).click()
                alert = self.driver.switch_to.alert
                alert.accept()
                self.business_membership_click(Businessname, BusinessUshjaid, Address, State, City, Zip, Phone, Fax,
                                               Email, Website, Media, Affliations, Typeofbusiness, Businessowner,
                                               BusinessOwnerUshjaid, Contactfname, Contactlname, Contactptitle,
                                               ContactUSHJAid, AddressContact, CityContact, StateContact, ZipContact,
                                               PhoneContact, FaxContact, EmailContact, AlternateContactname,
                                               AlternateContacttitle, AlternateContactphone, AlternateContactemail,Signature,
                                               creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)

       except :

          print("NO ALERT")
          self.business_membership_click(Businessname,BusinessUshjaid,Address,State,City,Zip,Phone,Fax,Email,Website,Media,Affliations,Typeofbusiness,Businessowner, BusinessOwnerUshjaid,Contactfname,Contactlname,Contactptitle,ContactUSHJAid,AddressContact,CityContact,StateContact,ZipContact,PhoneContact,FaxContact,EmailContact,AlternateContactname,AlternateContacttitle,AlternateContactphone,AlternateContactemail,Signature,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)

