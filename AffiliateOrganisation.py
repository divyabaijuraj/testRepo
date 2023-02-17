import os

from charset_normalizer import detect
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from detect_delimiter import detect
from string import ascii_letters

from utilities.base_class import BaseFunc
import time





class AffiliateOrganisation(BaseFunc):
    text_alertskip_xpath = "//button[@title='Skip']"
    ########### Organisation Information ##############
    link_affiliateorganization_xpath = "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12']//child::p[contains(text(),'Affiliate Organization')]"

    textbox_association_name_xpath="//*[@name='name']"
    textbox_address_xpath="//*[@name='address']"
    textbox_city_xpath="//*[@name='city']"
    textbox_state_xpath="//*[@name='state']"
    textbox_zip_xpath="//*[@name='zip']"
    textbox_phone_xpath="//*[@name='phone']"
    textbox_fax_xpath="//*[@name='fax']"
    textbox_email_xpath="//*[@name='email']"
    textbox_website_xpath = "//*[@name='website']"
    textbox_president_xpath= "//*[@name='president']"
    textbox_presidentId_xpath="//*[@name='presidentId']"
    button_continue_xpath="//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained makeStyles-nextStep-219 MuiButton-containedPrimary'  or @type='button']//child::span[contains(text(),'Continue')]"

    #################   Affiliate Contact person Information ############################
    textbox_affiliate_contactfname_name = "contactFirstName"
    textbox_affiliate_contactlname_name = "contactLastName"
    textbox_affiliate_contactperson_name = "contactPersonTitle"
    textbox_affiliate_ushjaid2_name = "contactUshjaId"
    textbox_affiliate_address_xpath = "//*[@name='address']"
    textbox_affiliate_city_xpath = "//*[@name='city']"
    dropdown_affiliate_state_id = "mui-component-select-state"
    textbox_affiliate_zip_xpath = "//*[@name='zip']"
    textbox_affiliate_phone_xpath = "//*[@name='phone']"
    textbox_affiliate_fax_xpath = "//*[@name='fax']"
    textbox_affiliate_email_xpath = "//*[@name='email']"
    textbox_affiliate_alternatefname_name = "alternateContactName"
    textbox_affiliate_alternatectitle_name = "alternateContactTitle"
    textbox_affiliate_alternatephone_name = "alternateContactPhone"
    textbox_affiliate_alternateemail_name = "alternateContactEmail"
    button_affiliate_contactinfocontinue_xpath="//*[starts-with(@class,'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10')]//child::button/span[contains(text(),'Continue')]"
    ############# Signature  ###################
    textbox_signature_xpath="//*[@class='MuiInputBase-input MuiOutlinedInput-input' and @type='text']"
    button_signature_xpath="//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10']//child::button/span[contains(text(),'Continue')]"

    ################ Committe Representation Area  #######################
    dropdown1_board_of_directors_xpath=  "//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[4]"

    dropdown2_members_on_board_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[5]"

    input_members_on_board_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[5]//input"
    dropdown3_organisation_bylaws_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[9]"
    dropdown3_organisation_bylaws_no_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[8]"

    dropdown4_organisation_nonprofit_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[14]"
    dropdown4_organisation_nonprofit_no_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[12]"

    dropdown5_organisation_shows_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[18]"
    dropdown5_organisation_shows_no_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[16]"

    dropdown_annual_education_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[22]"
    dropdown_annual_education_no_xpath="//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-3']//descendant::div[20]"

    button_committe_rep_xpath="//div[@class ='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10']//child::button/span[contains(text(),'Continue')]"

    ##### Organisation Information Survey
    ##"//div[@class='MuiFormControl-root MuiTextField-root makeStyles-textControl-505']//child::div/input[@name='howManyIndividualMembers']"
    dropdown_individual_member_id="mui-component-select-doesOrgHasMembers"
    input_no_of_members_name="howManyIndividualMembers"
    input_professional_breakdown="professionalPercentageBreakdown"
    input_junior_breakdown= "juniorPercentageBreakdown"
    input_amateur_breakdown_name="amateurPercentageBreakdown"
    checkbox_categorize_org_name="selectedCategory"
    input_othercategory_name="otherSelectedCategoryExplanation"
    input_org_primaryserve_name="whatUshjaZoneDoesYourOrganizationPrimarilyServe"
    dropdown_newsletter_id="mui-component-select-doYouSendNewsLetterToMembers"
    radio_newsletter_electronic_xpath="//*[@name='electronicOrPrint' and @value='Electronic']"
    radio_newsletter_print_xpath="//*[@name='electronicOrPrint' and @value='Print']"
    input_issues_peryear_name='newsIssuesYear'
    input_mission_statement_name="orgMissionStatementOrPurpose"
    checkbox_participation_name="selectedParticipations"

    input_other_pgm_name="otherParticipationCategoryExplanation"
    checkbox_educationpgm_name="selectedHosting"
    input_other_edupgm_name="otherSelectedHostingExplanation"
    input_additionalpgm_name="additionalPrograms"
    dropdown_educational_programs_id="mui-component-select-doYouOfferEducationalProgramsOrAactivities"
    input_desc_name="educationalProgramsOrActivitiesDescription"
    input_comments_name="additionalComments"
    button_choosefile_class="MuiButtonBase-root MuiButton-root MuiButton-text makeStyles-uploadButton-474"
    button_orginfo_survey_xpath = "//button[contains(@class,'MuiButtonBase-root MuiButton-root MuiButton-contained makeStyles-nextStep-')] //child::span[contains(text(),'Continue')]"
    ########  Make Payment  ##########

    #radio_add_creditcard_xpath="//div[contains(@class,'MuiBox-root MuiBox-root-745')]//span[@class='MuiIconButton-label']//child::input[contains(@class,'PrivateSwitchBase-input-')]"
    radio_add_creditcard_xpath="//p[@class='MuiTypography-root MuiTypography-body1' and contains(text(),'Add Credit Card')]//preceding-sibling::span/span/input"
    textbox_firstname_name = "firstName"
    textbox_lastname_name = "lastName"
    textbox_address_name = "line1"
    textbox_postalcode_name = "postal_code"
    textbox_cardno_xpath = "//input[@placeholder='Card number']"
    textbox_mmdd_xpath = "// input[ @ id = 'card-expiry']"
    textbox_cvc_xpath = "//input[@id='cvc']"
    checkbox_savecard_name="saveMyCard"
    button_pay_xpath = "//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-text makeStyles-nextStep-231'  or @type='button']//child::span[contains(text(),'Pay')]"



    ############## Order Confirmation ########################
    text_affiliateorg_conf_xapth="//h4[contains(text(), 'Affiliate Organization Application Successful')]"
    aff_close_button_xpath = "//*[@class='MuiButtonBase-root MuiIconButton-root'  and @aria-label='close']"

   ##################Affiliation Quick Action###################

    aff_text_aftersubmssion_xpath = "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12']//child::p[contains(text(),'Affiliate Organization')]"
    aff_text_date_xpath = "//*[@id='root']/div[1]/div[2]/main/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/p"





    def affiliate_Organisation(self,AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile):

       ##############  Organisation Information ###################################
        print("in affiliate ORG")
        #self.wait_presence_of_element_located(By.XPATH,self.link_affiliateorganization_xpath).click()
        time.sleep(2)
        if (AssociationName ==""):

            print("Enter valid AssociateName ")
            assert False

        else:
           self.wait_presence_of_element_located(By.XPATH, self.textbox_association_name_xpath).send_keys(AssociationName)

        if(Address == ""):

            print("Enter valid ADDRESS name")
            assert False

        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_address_xpath).send_keys(Address)
        if(City == "") :

            print("Enter valid CITY name")
            assert False
        else:
             self.wait_presence_of_element_located(By.XPATH, self.textbox_city_xpath).send_keys(City)

        if (State == ""):

            print("Enter valid STATE name")
            assert False
        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_state_xpath).send_keys(State)

        if (Zip == ""):

            print("Enter valid STATE name")
            assert False
        else:
             self.wait_presence_of_element_located(By.XPATH, self.textbox_zip_xpath).send_keys(Zip)

        if (Phone == ""):

            print("Enter valid STATE name")
            assert False
        else:
           self.wait_presence_of_element_located(By.XPATH, self.textbox_phone_xpath).send_keys(Phone)

        if (Fax == ""):

            print("Enter valid STATE name")
            pass
        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_fax_xpath).send_keys(Fax)

        if(Email == ""):
            print("Enter valid Email ")
            assert False
        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_email_xpath).send_keys(Email)

        if(Website =="") :
            print("Enter valid Website")
            pass
        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_website_xpath).send_keys(Website)

        if (President == ""):
            print("Enter valid President")
            assert False
        else:

            self.wait_presence_of_element_located(By.XPATH, self.textbox_president_xpath).send_keys(President)

        if (PresidentUSHJAID == ""):
            print("Enter valid PresidentUSHJAID")
            pass
        else:
            self.wait_presence_of_element_located(By.XPATH, self.textbox_presidentId_xpath).send_keys(PresidentUSHJAID)

        self.wait_presence_of_element_located(By.XPATH, self.button_continue_xpath).click()

        time.sleep(2)

       ################## Affiliate Contact Person Information #########################


        time.sleep(2)

        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_contactfname_name).send_keys(ContactFirstName)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_contactlname_name).send_keys(ContactLastName)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_contactperson_name).send_keys(ContactPersonTitle)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_ushjaid2_name).send_keys(ContactUSHJAID)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_address_xpath).send_keys(ContactAddress)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_city_xpath).send_keys(ContactCity)
        self.wait_presence_of_element_located(By.ID, self.dropdown_affiliate_state_id).click()

        time.sleep(2)
        statename = "Arizona"
        self.wait_presence_of_element_located(By.XPATH, "//li[contains(text(),'" + ContactState + "')]").click()
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_zip_xpath).send_keys(ContactZip)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_phone_xpath).send_keys(ContactPhone)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_fax_xpath).send_keys(ContactFax)
        self.wait_presence_of_element_located(By.XPATH, self.textbox_affiliate_email_xpath).send_keys(ContactEmail)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_alternatefname_name).send_keys(AlternateContactName)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_alternatectitle_name).send_keys(AlternateContactTitle)
        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_alternatephone_name).send_keys(AlternateContactPhone)

        self.wait_presence_of_element_located(By.NAME, self.textbox_affiliate_alternateemail_name).send_keys(AlternateContactEmail)

        self.wait_presence_of_element_located(By.XPATH, self. button_affiliate_contactinfocontinue_xpath).click()
        time.sleep(2)
        ####################  Signature  ###############

        self.wait_presence_of_element_located(By.XPATH, self.textbox_signature_xpath).send_keys(Signature)
        self.wait_presence_of_element_located(By.XPATH,self.button_signature_xpath).click()
        time.sleep(2)

       ######################  Committee Representation Criteria####################
        option = 'Yes'
        # Signature,,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity
        # if(option=="Yes"):
        #     self.option_check_yes(option)
        #
        # else:
        #     self.option_check_no(option)
        if(BoardOfDirectors == 'Yes'):
            self.wait_presence_of_element_located(By.XPATH, self.dropdown1_board_of_directors_xpath).click()
            self.wait_presence_of_element_located(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + BoardOfDirectors + "')]").click()
            self.wait_presence_of_element_located(By.XPATH, self.dropdown2_members_on_board_xpath).click()

            self.wait_presence_of_element_located(By.XPATH, self.input_members_on_board_xpath).send_keys("1")
        else:
            self.wait_presence_of_element_located(By.XPATH, self.dropdown1_board_of_directors_xpath).click()
            self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + BoardOfDirectors + "')]").click()

        if(BoardOfDirectors == 'Yes'):
            self.wait_presence_of_element_located(By.XPATH, self.dropdown3_organisation_bylaws_xpath).click()
            if(Bylaws == 'Yes'):
                     self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + Bylaws + "')]").click()
            elif(Bylaws == 'No'):
                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + Bylaws + "')]").click()

            time.sleep(2)
        else:
            self.wait_presence_of_element_located(By.XPATH, self.dropdown3_organisation_bylaws_no_xpath).click()
            if (Bylaws == 'Yes'):
                self.wait_presence_of_element_located(By.XPATH,
                                                      "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + Bylaws + "')]").click()
            elif (Bylaws == 'No'):
                self.wait_presence_of_element_located(By.XPATH,
                                                      "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + Bylaws + "')]").click()

            time.sleep(2)


            # self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + Bylaws + "')]").click()
            # time.sleep(2)
        if(BoardOfDirectors == 'Yes'):
            self.wait_presence_of_element_located(By.XPATH, self.dropdown4_organisation_nonprofit_xpath).click()
            time.sleep(2)
            if(OrgNonProfit == 'Yes'):
                 self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + OrgNonProfit + "')]").click()
            elif(OrgNonProfit == 'No'):
                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()


        else:
            self.wait_presence_of_element_located(By.XPATH, self.dropdown4_organisation_nonprofit_no_xpath).click()
            time.sleep(2)
            if (OrgNonProfit == 'Yes'):
                self.wait_presence_of_element_located(By.XPATH,
                                                      "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + OrgNonProfit + "')]").click()
            elif (OrgNonProfit == 'No'):
                self.wait_presence_of_element_located(By.XPATH,
                                                      "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()

            time.sleep(2)

        if(BoardOfDirectors == 'Yes'):
            self.wait_presence_of_element_located(By.XPATH, self.dropdown5_organisation_shows_xpath).click()
            time.sleep(2)
            if(SanctionedShows == 'Yes'):
                    self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + SanctionedShows + "')]").click()
            else:

                    self.wait_presence_of_element_located(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()
            time.sleep(2)

        else:

            self.wait_presence_of_element_located(By.XPATH, self.dropdown5_organisation_shows_no_xpath).click()
            time.sleep(2)
            if (SanctionedShows == 'Yes'):
                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[contains(text(),'" + SanctionedShows + "')]").click()
            else:

                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()
            time.sleep(2)


            #self.wait_presence_of_element_located(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()
        #

        if(BoardOfDirectors == 'Yes'):
            self.wait_presence_of_element_located(By.XPATH, self.dropdown_annual_education_xpath).click()
            if(EducationActivity == 'Yes'):

                    self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='true']").click()
            else:
                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()

            time.sleep(2)
        else:
            self.wait_presence_of_element_located(By.XPATH, self.dropdown_annual_education_no_xpath).click()
            if (EducationActivity == 'Yes'):

                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='true']").click()
            else:
                self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()

            time.sleep(2)
            #self.wait_presence_of_element_located(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//descendant::li[@data-value='false']").click()
        self.wait_presence_of_element_located(By.XPATH,self.button_committe_rep_xpath).click()




    # ########################################################################
    #
    #    #  #############Organization Information Survey#########
    #    #
        self.wait_presence_of_element_located(By.ID,self. dropdown_individual_member_id).click()
        time.sleep(2)


        self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button' and contains(text(),'" + IndividualMembers + "')]").click()
        time.sleep(4)
        if(IndividualMembers=='Yes'):
                self.wait_presence_of_element_located(By.NAME,self.input_no_of_members_name).send_keys(MembersNo)
                time.sleep(2)
                self.wait_presence_of_element_located(By.NAME,self.input_professional_breakdown).send_keys(Professional)

                time.sleep(2)
                self.wait_presence_of_element_located(By.NAME,self.input_junior_breakdown).send_keys(Junior)

                time.sleep(2)
                self.wait_presence_of_element_located(By.NAME,self.input_amateur_breakdown_name).send_keys(Amateur)

                time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        time.sleep(10)
        print("type of category:",type(Category_orgCgeckbox))

        if (Category_orgCgeckbox is None):
              assert False

        delimeter = detect(Category_orgCgeckbox, whitelist=[","])
        if(delimeter is None):
            self.wait_presence_of_element_located(By.XPATH,
                                                  "//*[@class='MuiTypography-root MuiFormControlLabel-label MuiTypography-body1']//child::p[text()='" + Category_orgCgeckbox + "']//preceding ::span[@class='MuiIconButton-label']/input[@type='checkbox']").click()
            if (Category_orgCgeckbox == 'Other'):
                self.wait_presence_of_element_located(By.XPATH,
                                                      "/html/body/div[6]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[4]/label/span[2]/p").click()
                self.wait_presence_of_element_located(By.XPATH, self.input_othercategory_name).send_keys("testing454")
        else:
             categorylist = Category_orgCgeckbox.split(',')
             for category in categorylist:
                print("category",category)
                time.sleep(2)

                self.wait_presence_of_element_located(By.XPATH, "//p[contains(text(),'" + category + "')]").click()

                time.sleep(2)
                if(category == 'Other'):
                    self.wait_presence_of_element_located(By.XPATH,  "/html/body/div[6]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[4]/label/span[2]/p").click()
                    #self.wait_presence_of_element_located(By.XPATH,"//*[@class='MuiTypography-root MuiFormControlLabel-label MuiTypography-body1']//child::p[text()='" + category + "']//preceding ::span[@class='MuiIconButton-label']/input[@type='checkbox']").click()
                    self.wait_presence_of_element_located(By.XPATH,self.input_othercategory_name).send_keys("testing454")



        self.wait_presence_of_element_located(By.NAME,self.input_org_primaryserve_name).send_keys(PrimarlyServe)
        self.wait_presence_of_element_located(By.ID,self.dropdown_newsletter_id ).click()
        time.sleep(2)

        value = 'Print'
        if (Newsletter == 'Yes'):
            print('inside if ')
            self.wait_presence_of_element_located(By.XPATH, "//*[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + Newsletter + "')]").click()
            time.sleep(2)
            if  (NewsletterOption =='Electronic'):
               print("INSIDE SECOND IF")
               self.wait_presence_of_element_located(By.XPATH,self.radio_newsletter_electronic_xpath).click()

               time.sleep(2)
               self.wait_presence_of_element_located(By.NAME, self.input_issues_peryear_name).send_keys("2")
               time.sleep(2)
            elif(NewsletterOption=='Print'):
                self.wait_presence_of_element_located(By.XPATH, self.radio_newsletter_print_xpath).click()
                self.wait_presence_of_element_located(By.NAME, self.input_issues_peryear_name).send_keys("2")
                time.sleep(2)
        else:
            self.wait_presence_of_element_located(By.XPATH,"//*[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + Newsletter + "')]").click()


        self.wait_presence_of_element_located(By.NAME,self.input_mission_statement_name).send_keys(missionstatement)
        checkbox_participation=self.wait_presence_of_all_elements_located(By.NAME,self.checkbox_participation_name)
        print("*********",checkbox_participation[4])

        if(Participation_checkbox is None):
           assert False

        else:
            delimeter = detect(Participation_checkbox, whitelist=[","])
            if(delimeter  is None):

                self.wait_presence_of_element_located(By.XPATH, "//p[contains(text(),'" + Participation_checkbox + "')]").click()

                time.sleep(2)
                if (Participation_checkbox == 'Other'):
                    self.wait_presence_of_element_located(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[8]/div/div/div[5]/label/span[2]/p").click()
                    time.sleep(2)
                    self.wait_presence_of_element_located(By.NAME, self.input_other_pgm_name).send_keys("testing")
                    time.sleep(2)
            else:
                 Participationlist = Participation_checkbox.split(',')

                 for plist in Participationlist:
                    print("plist", plist)
                    time.sleep(2)

                    self.wait_presence_of_element_located(By.XPATH, "//p[contains(text(),'" + plist + "')]").click()
                    time.sleep(2)
                    if(plist == 'Other'):
                        self.wait_presence_of_element_located(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[8]/div/div/div[5]/label/span[2]/p").click()
                        time.sleep(2)
                        self.wait_presence_of_element_located(By.NAME,self.input_other_pgm_name).send_keys("testing")
                        time.sleep(2)



        print("EducationCheckbox",type(EducationCheckbox))

        if(EducationCheckbox is None):
            assert False
        else:
            delimeter = detect(EducationCheckbox, whitelist=[","])
            if (delimeter is None):
                self.wait_presence_of_element_located(By.XPATH,"//p[contains(text(),'" + EducationCheckbox + "')]").click()
                if (EducationCheckbox == 'Other'):
                    self.wait_presence_of_element_located(By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[10]/div/div/div[7]/label/span[1]/span[1]/input").click()
                    time.sleep(2)
                    self.wait_presence_of_element_located(By.NAME, self.input_other_edupgm_name).send_keys("testing123")
            else:

                Educationlist=EducationCheckbox.split(',')
                for elist in Educationlist:
                        print("elist",elist)
                        time.sleep(2)
                        if (elist == 'Other'):
                            self.wait_presence_of_element_located(By.XPATH,"/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[10]/div/div/div[7]/label/span[1]/span[1]/input").click()
                            time.sleep(2)
                            self.wait_presence_of_element_located(By.NAME, self.input_other_edupgm_name).send_keys("testing123")
                        else:
                            self.wait_presence_of_element_located(By.XPATH,"//p[contains(text(),'" + elist + "')]").click()

                        time.sleep(2)

        # else:
        #     self.wait_presence_of_element_located(By.XPATH, "//p[contains(text(),'" + EducationCheckbox + "')]").click()
        #     if(EducationCheckbox == 'Other'):
        #         self.wait_presence_of_element_located(By.NAME, self.input_other_edupgm_name).send_keys("testing123")
        print("AFTER IF  ELSE:")
        self.wait_presence_of_element_located(By.NAME, self.input_additionalpgm_name).send_keys(NeedsAffiliateOrg)
        time.sleep(2)
        self.wait_presence_of_element_located(By.ID,self.dropdown_educational_programs_id).click()
        time.sleep(2)
        print("Education programs:",EducationPrograms)

        print("Additional comments:", AdditionalComments)

        self.wait_presence_of_element_located(By.XPATH,"//*[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + EducationPrograms + "')]").click()
        time.sleep(2)
        if(EducationPrograms =='Yes'):
             print("Inside IF ****")
             if(EducationPrograms  is None):
                 assert False
             else:
                 self.wait_presence_of_element_located(By.NAME,self.input_desc_name).send_keys(EducationPrograms)
                 time.sleep(2)
        else:
            pass

        self.wait_presence_of_element_located(By.NAME,self.input_comments_name ).send_keys(AdditionalComments)
        time.sleep(2)


        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)


        choosefile=self.wait_presence_of_element_located(By.XPATH,"//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11']//child::div[contains(@class,'MuiBox-root MuiBox-root-')]//child::input[@type='file']")
        choosefile.send_keys(ChooseFile)

        time.sleep(6)

        # self.wait_presence_of_element_located(By.XPATH,self.button_orginfo_survey_xpath).click()
        # time.sleep(2)
    #
    #     ###################  Make Payment ##########################
    #
      #  self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    def make_payment(self,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew):

            self.wait_presence_of_element_located(By.XPATH, self.button_orginfo_survey_xpath).click()
            time.sleep(2)
            element=  self.wait_presence_of_element_located(By.XPATH, self.radio_add_creditcard_xpath)
            element.location_once_scrolled_into_view
            if element.is_selected():
                pass
            else:
                 element.click()
                 time.sleep(2)

            self.wait_presence_of_element_located(By.NAME, self.textbox_firstname_name).send_keys(creditcard_firstname)
            self.wait_presence_of_element_located(By.NAME, self.textbox_lastname_name).send_keys(Creditcard_lastname)
            self.wait_presence_of_element_located(By.NAME, self.textbox_address_name).send_keys(Creditcard_address)

            self.wait_presence_of_element_located(By.NAME, self.textbox_postalcode_name).send_keys(Creditcard_postalcode)
            self.wait_presence_of_element_located(By.XPATH, self.textbox_cardno_xpath).send_keys(Creditcard_cardno)
            self.wait_presence_of_element_located(By.XPATH, self.textbox_mmdd_xpath).send_keys(Creditcard_mmyy)
            self.wait_presence_of_element_located(By.XPATH, self.textbox_cvc_xpath).send_keys(Creditcard_cvc)

            savecard_name='No'
            if(savecard_name == 'Yes'):
                self.wait_presence_of_element_located(By.NAME, self.checkbox_savecard_name).click()
            else:
                pass

            self.wait_presence_of_element_located(By.XPATH, self.button_pay_xpath).click()
            time.sleep(2)

            #############Order Confirmation###################
            aff_confirmation=self.wait_presence_of_element_located(By.XPATH,self.text_affiliateorg_conf_xapth)
            print(aff_confirmation.text)
            self.aff_confirmation=  aff_confirmation.text
            time.sleep(2)

            #self.wait_presence_of_element_located(By.XPATH, "//*[contains(text(),'AFFILIATE MEMBERSHIP IS NOT VALID FOR COMPETITIONS! For competitions purposes, ')]" ).click()
            #self.wait_presence_of_element_located(By.XPATH,"//*[contains(text(),'Affiliate Organization Application Successful')]")
            time.sleep(4)
            self.driver.refresh()
            #self.wait_presence_of_element_located(By.XPATH, self.aff_close_button_xpath).click()

            time.sleep(15)
           #######Affiliate Organisation Quick Action
            self.driver.execute_script("window.scroll(0, 0);")
            time.sleep(15)
            affiliateorg = self.wait_presence_of_element_located(By.XPATH, self.aff_text_aftersubmssion_xpath)
            time.sleep(10)
            self.affiliateorg = affiliateorg.text

            aff_date= self.wait_presence_of_element_located( By.XPATH,self.aff_text_date_xpath)

            self.aff_date=aff_date.text
            print (aff_date.text)
            if(self.aff_date is  None) :
                assert False
            else:
                assert True

    def alertorg_present(self,AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws	,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile,creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew
):

        try:

            self.wait_presence_of_element_located(By.XPATH, self.text_alertskip_xpath).click()

        except TimeoutException:

            print("Time out exception")
            self.wait_presence_of_element_located(By.XPATH, self.link_affiliateorganization_xpath).click()
            time.sleep(2)
            self.affiliate_Organisation(AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile)
            self.make_payment(creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)


        else:
            print("OK********************")
            self.wait_presence_of_element_located(By.XPATH, self.link_affiliateorganization_xpath).click()
            time.sleep(2)
            self.affiliate_Organisation(AssociationName,Address,City,State,Zip,Phone,Fax,Email,Website,President,PresidentUSHJAID,ContactFirstName,ContactLastName,ContactPersonTitle,ContactUSHJAID,ContactAddress,ContactCity,ContactState,ContactZip,ContactPhone,ContactFax,ContactEmail,AlternateContactName,AlternateContactTitle,AlternateContactPhone,AlternateContactEmail,Signature,BoardOfDirectors,Bylaws,OrgNonProfit,SanctionedShows,EducationActivity,IndividualMembers,MembersNo,Professional,Junior,Amateur,Category_orgCgeckbox,PrimarlyServe,Newsletter,NewsletterOption,IssuesPerYear,missionstatement,Participation_checkbox,EducationCheckbox,NeedsAffiliateOrg,EducationPrograms,EducationDescription,AdditionalComments,ChooseFile)
            self.make_payment(creditcard_firstname,Creditcard_lastname,Creditcard_address,Creditcard_postalcode,Creditcard_cardno,Creditcard_mmyy,Creditcard_cvc,Savemycard,Autorenew)
