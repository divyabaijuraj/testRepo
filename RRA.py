import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.base_class import BaseFunc
from selenium.webdriver.support import expected_conditions as EC


class RecognizedRdingAcademy(BaseFunc):
     text_alertskip_xpath = "//button[@title='Skip']"
     #################RRA My Programs,ENROLL BUTTON
     img_myprogram_xpath="//img[contains(@class,'makeStyles-svg-') and @alt='program']"
     text_MyUSHJA_xpath="//*[contains(text(),'My USHJA')]"

     myprograms_rra_enroll_xpath="//tr[contains(@class,'MuiTableRow-root makeStyles-expantableHeader-')]//th/p[contains(text(),'USHJA Recognized Riding Academy')]//parent::th//following-sibling::td/div/button"

     ########### 1st form GENERAL  #############################
     textbox_academyname_name="academyName"
     textbox_academyOwner_name="academyOwner"
     radio_isOwnerEighteenYearOrOld_yes_xpath="//*[@name='isOwnerEighteenYearOrOld'  and @value='true']"
     radio_isOwnerEighteenYearOrOld_no_xpath = "//*[@name='isOwnerEighteenYearOrOld'  and @value='false']"
     ### facility
     textbox_facilityAddress_name="facilityAddress"
     textbox_facilityCity_name="facilityCity"
     dropdown_facilitystate_xpath="//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input'  and @role='button'  and @id='mui-component-select-facilityState']"
     textbox_facilityZip_name="facilityZip"
     checkbox_mailSameAsFacility_name="mailSameAsFacility"

     ###Mailing address

     textbox_mailing_name="mailAddress"
     textbox_mailCity_name="mailCity"
     dropdown_mailstate_id="mui-component-select-mailState"
     textbox_mailphone_xpath="//input[@name='phone']"
     textbox_mailcell_xpath="//input[@name='cell']"
     textbox_mailemail_xpath="//input[@name='email']"
     textbox_mail_website_xpath="//input[@name='website']"
     textbox_applicantname_name="applicantName"
     textbox_applicanttitle_name="applicantTitle"
     textbox_applicantemail_name="applicantEmail"
     textbox_applicantphone_name="applicantPhone"
     ##########  staff details
     textbox_staffName_name="staffName"
     textbox_staffTitle_name="staffTitle"
     textbox_staffEmail_name="staffEmail"
     textbox_staffUshjaId_name="staffUshjaId"

     textbox_zone_xpath="//input[@name='zone']"
     radio_isCredentializedInstructor_yes_xpath="//input[@name='isCredentialedInstructor' and @value='true']"
     radio_isCredentializedInstructor_no_xpath = "//input[@name='isCredentialedInstructor' and @value='false']"
     textbox_icStaffUshjaId_name="icStaffUshjaId"
     button_facility_xpath="//span[contains(text(),'Facility')]//ancestor::button[@type='button']"

     ##################### 2nd form  FACILITY #####################
     textarea_interest_USHJA_xpath="//textarea[@name='interests']"
     textarea_academyPrograms_xpath="//textarea[@name='academyPrograms']"

     radio_isDailyfeedAndFreshwaterYes_xpath="//input[@name='isDailyfeedAndFreshwater'  and @value='true']"
     radio_isDailyfeedAndFreshwaterNo_xpath="//input[@name='isDailyfeedAndFreshwater'  and @value='false']"

     radio_isWeatherAppropriateYes_xpath= "//input[@name='isWeatherAppropriate'  and @value='true']"
     radio_isWeatherAppropriateNo_xpath = "//input[@name='isWeatherAppropriate'  and @value='false']"

     radio_isRoutineVaterinarianYes_xpath=  "//input[@name='isRoutineVaterinarian'  and @value='true']"
     radio_isRoutineVaterinarianNo_xpath = "//input[@name='isRoutineVaterinarian'  and @value='false']"

     radio_isDailyTurnoutOpportunitiesYes_xpath=  "//input[@name='isDailyTurnoutOpportunities'  and @value='true']"
     radio_isDailyTurnoutOpportunitiesNo_xpath = "//input[@name='isDailyTurnoutOpportunities'  and @value='false']"

     radio_isDewormingScheduleYes_xpath=   "//input[@name='isDewormingSchedule'  and @value='true']"
     radio_isDewormingScheduleNo_xpath =  "//input[@name='isDewormingSchedule'  and @value='false']"

     radio_isSafeRidingAreaYes_xpath=    "//input[@name='isSafeRidingArea'  and @value='true']"
     radio_isSafeRidingAreaNo_xpath = "//input[@name='isSafeRidingArea'  and @value='false']"

     radio_isThereCoveredLocationYes_xpath=  "//input[@name='isThereCoveredLocation'  and @value='true']"
     radio_isThereCoveredLocationNo_xpath = "//input[@name='isThereCoveredLocation'  and @value='false']"

     radio_isThereRestroomsPermanent_xpath=  "//input[@name='isThereRestrooms'  and @value='permanent']"
     radio_isThereRestroomstemporary_xpath="//input[@name='isThereRestrooms'  and @value='temporary']"
     radio_isThereRestroomsnone_xpath="//input[@name='isThereRestrooms'  and @value='none']"

     radio_isThereofficeYes_xpath="//input[@name='isThereOffice'  and @value='true']"
     radio_isThereofficeNo_xpath = "//input[@name='isThereOffice'  and @value='false']"

     radio_isThereClassroomYes_xpath=    "//input[@name='isThereClassroom'  and @value='true']"
     radio_isThereClassroomNo_xpath = "//input[@name='isThereClassroom'  and @value='false']"

     radio_areThereLockerYes_xpath="//input[@name='areThereLocker'  and @value='true']"
     radio_areThereLockerNo_xpath = "//input[@name='areThereLocker'  and @value='false']"

     radio_isThereAdequateParkingYes_xpath=  "//input[@name='isThereAdequateParking'  and @value='true']"
     radio_isThereAdequateParkingNo_xpath = "//input[@name='isThereAdequateParking'  and @value='false']"

     radio_isThereClubroomYes_xpath="//input[@name='isThereClubroom'  and @value='true']"
     radio_isThereClubroomNo_xpath = "//input[@name='isThereClubroom'  and @value='false']"

     radio_isThereInternetYes_xpath="//input[@name='isThereInternet'  and @value='true']"
     radio_isThereInternetNo_xpath="//input[@name='isThereInternet'  and @value='false']"

     button_operational_xpath="//span[contains(text(),'Operational')]//ancestor::button[@type='button']"

     ######################  3rd form OPERTIONAL  ########################

     textbox_noOfParticipants_name = "noOfParticipants"
     textbox_noOfHunters_name = "noOfHunters"
     textarea_typesOfLessons_name = "typesOfLessons"
     radio_areThereInstructionLevelYes_xpath =  "//input[@name='areThereInstructionLevel'   and @value='true']"
     radio_areThereInstructionLevelNo_xpath = "//input[@name='areThereInstructionLevel'   and @value='false']"

     textarea_levelsOfLessons_name="levelsOfLessons"

     radio_doesAcademyOfferNonrideInstructionYes_xpath  = "//input[@name='doesAcademyOfferNonrideInstruction'  and @value='true']"
     radio_doesAcademyOfferNonrideInstructionNo_xpath  =  "//input[@name='doesAcademyOfferNonrideInstruction'  and @value='false']"
     textarea_academyOfferedNonrideInstruction_name="academyOfferedNonrideInstruction"
     textbox_ratioOfInstructor_name="ratioOfInstructor"
     textbox_noOfSchoolHorses_name="noOfSchoolHorses"
     radio_isScheduleDailyBreakYes_xpath =  "//input[@name='isScheduleDailyBreak'  and @value='true']"
     radio_isScheduleDailyBreakNo_xpath =   "//input[@name='isScheduleDailyBreak'  and @value='false']"

     button_services_xpath="//span[contains(text(),'Services')]//ancestor::button[@type='button']"



     ###################  SERVICES#################################

     radio_doesAcademyOfferSocialServicesYes_xpath = "//input[@name='doesAcademyOfferSocialServices'  and @value='true']"
     radio_doesAcademyOfferSocialServicesNo_xpath = "//input[@name='doesAcademyOfferSocialServices'  and @value='false']"
     textarea_academyOfferedSocialServices_name="academyOfferedSocialServices"

     textbox_otherAspectsOfAcademyOperation_name="otherAspectsOfAcademyOperation"
     button_safety_xpath="//span[contains(text(),'Safety')]//ancestor::button[@type='button']"

     ###########################   SAFETY  ################################
     radio_areRequireToWearHelmetYes_xpath = "//input[@name='areRequireToWearHelmet'  and @value='true']"
     radio_areRequireToWearHelmetNo_xpath = "//input[@name='areRequireToWearHelmet'  and @value='false']"

     radio_doesRequireToSignReleaseOfLiabilityYes_xpath  =   "//input[@name='doesRequireToSignReleaseOfLiability'  and @value='true']"
     radio_doesRequireToSignReleaseOfLiabilityNo_xpath = "//input[@name='doesRequireToSignReleaseOfLiability'  and @value='false']"

     radio_doesAcademyCarryInsuranceYes_xpath  =   "//input[@name='doesAcademyCarryInsurance'  and @value='true']"
     radio_doesAcademyCarryInsuranceNo_xpath = "//input[@name='doesAcademyCarryInsurance'  and @value='false]"
     button_choosefilelocate_xpath="//span[contains(text(),'Choose File')]"
     button_choose_file_xpath = "//span[contains(text(),'Choose File')]//parent::button"

     radio_isThereSafetyPlanYes_xpath = "//input[@name='isThereSafetyPlan'   and @value='true']"
     radio_isThereSafetyPlanNo_xpath = "//input[@name='isThereSafetyPlan'   and @value='false']"

     radio_isTelephoneAvailableYes_xpath  =  "//input[@name='isTelephoneAvailable'   and @value='true']"
     radio_isTelephoneAvailableNo_xpath  = "//input[@name='isTelephoneAvailable'   and @value='false']"

     radio_isStockedYes_xpath=  "//input[@name='isStocked'   and @value='true']"
     radio_isStockedNo_xpath = "//input[@name='isStocked'   and @value='false']"

     radio_isThereStaffFamiliarWithCprYes_xpath = "//input[@name='isThereStaffFamiliarWithCpr'   and @value='true']"
     radio_isThereStaffFamiliarWithCprNo_xpath = "//input[@name='isThereStaffFamiliarWithCpr'   and @value='false']"

     textarea_staffName_name ="staffName"

     button_Miscellaneous_xpath =  "//span[contains(text(),'Miscellaneous')]//ancestor::button[@type='button']"
     # ###########################################    6th form MISCELLANEOUS ###########################################


     time.sleep(4)

     radio_areThereMinStandardsForInstructorYes_xpath = "//input[@name='areThereMinStandardsForInstructor'  and @value='true']"
     radio_areThereMinStandardsForInstructorNo_xpath = "//input[@name='areThereMinStandardsForInstructor'  and @value='false']"
     textarea_StandardsForInstructor_xpath = "//textarea[@name='minStandardsForInstructor']"

     radio_isThereOpportunityForCareerDevelopmentYes_xpath = "//input[@name= 'isThereOpportunityForCareerDevelopment'  and @value='true']"
     textarea_opportunityForCareerDevelopment_xpath =   "//textarea[@name ='opportunityForCareerDevelopment']"
     radio_isThereOpportunityForCareerDevelopmentNo_xpath = "//input[@name= 'isThereOpportunityForCareerDevelopment'  and @value='false']"

     radio_doesAcademyAdvertiseForNewStudentsYes_xpath =  "//input[@name='doesAcademyAdvertiseForNewStudents'  and @value='true']"
     radio_doesAcademyAdvertiseForNewStudentsNo_xpath = "//input[@name='doesAcademyAdvertiseForNewStudents'  and @value='false']"
     textarea_howAcademyAdvertiseForNewStudents_xpath =   "//textarea[@name='howAcademyAdvertiseForNewStudents']"

     radio_isAcademyWillingToWorkWithUshjaYes_xpath = "//input[@name='isAcademyWillingToWorkWithUshja' and @value='true']"
     radio_isAcademyWillingToWorkWithUshjaNo_xpath = "//input[@name='isAcademyWillingToWorkWithUshja' and @value='false']"

     button_reference_xpath = "//span[contains(text(),'Reference')]//ancestor::button[@type='button']"

     ############################  REFERENCE##############################
     textarea_howToHearRRAProgram_name ="howToHearRRAProgram"

     textbox_referencename_xpath="//input[@name='name']"
     textbox_relationToApplicationRRA_name="relationToApplicationRRA"


     def rra_registration(self):
          #################RRA My Programs,ENROLL BUTTON
          time.sleep(2)
          #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
          time.sleep(2)
          #################RRA My Programs,ENROLL BUTTON
          print("OK REACHED ")


          time.sleep(20)
          #self.driver.execute_script("document.getElementByXpath('//div[contains(@class,'MuiBox-root MuiBox-root-301')]//div[1]').scrollIntoView();")
          myUshja=self.wait_presence_of_element_located(By.XPATH,self.text_MyUSHJA_xpath)
          self.driver.execute_script("arguments[0].scrollIntoView();",myUshja)
          time.sleep(10)
          self.wait_presence_of_element_located(By.XPATH,self.img_myprogram_xpath).click()
          time.sleep(2)
          self.wait_presence_of_element_located(By.XPATH,self.myprograms_rra_enroll_xpath).click()
          time.sleep(2)

         ######################### GENERAL  #######################


          self.wait_presence_of_element_located(By.NAME, self.textbox_academyname_name).click()
          time.sleep(2)
          self.wait_presence_of_element_located(By.NAME, self.textbox_academyname_name).send_keys("Academy1")
          time.sleep(2)
          self.wait_presence_of_element_located(By.NAME,self.textbox_academyOwner_name).send_keys("Academy Owner ")
          time.sleep(2)
          owner_older="Yes"
          if(owner_older == "Yes"):

                  self.wait_presence_of_element_located(By.XPATH, self.radio_isOwnerEighteenYearOrOld_yes_xpath ).click()
                  time.sleep(2)
          else:
                  self.wait_presence_of_element_located(By.XPATH,self.radio_isOwnerEighteenYearOrOld_no_xpath).click()
                  time.sleep(2)

          #self.general_facility()

          ####In general Facility details
          state_facility_name = 'Florida'
          name = self.wait_presence_of_element_located(By.NAME, self.textbox_facilityAddress_name).send_keys("fadd4")
          print(name, "*****************")
          time.sleep(2)
          self.wait_presence_of_element_located(By.NAME, self.textbox_facilityCity_name).send_keys("fname")
          time.sleep(2)
          self.wait_presence_of_element_located(By.XPATH, self.dropdown_facilitystate_xpath).click()
          time.sleep(4)
          self.wait_presence_of_element_located(By.XPATH,"//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + state_facility_name + "')]").click()
          time.sleep(2)
          self.wait_presence_of_element_located(By.NAME, self.textbox_facilityZip_name).send_keys("32013")
          time.sleep(2)


          #############  mail details
          statemail_name='Florida'
          checkbox_checked= self.wait_presence_of_element_located(By.NAME,self.checkbox_mailSameAsFacility_name)
          if checkbox_checked.get_attribute("value") != "true":
               checkbox_checked.click()
               self.wait_presence_of_element_located(By.NAME,self.textbox_mailing_name).send_keys("fadd4")
               self.wait_presence_of_element_located(By.NAME,self.textbox_mailCity_name).send_keys("fname")
               self.wait_presence_of_element_located(By.ID,self.dropdown_mailstate_id).click()
               time.sleep(2)
               self.wait_presence_of_element_located(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//child::li[contains(text(),'" + statemail_name + "')]").click()
               time.sleep(2)

          self.wait_presence_of_element_located(By.XPATH,self.textbox_mailphone_xpath).send_keys("989787675")
          self.wait_presence_of_element_located(By.XPATH, self.textbox_mailcell_xpath).send_keys("9454545455")
          self.wait_presence_of_element_located(By.XPATH, self.textbox_mailemail_xpath).send_keys("dbcham1983@gmail.com")
          self.wait_presence_of_element_located(By.XPATH, self.textbox_mail_website_xpath).send_keys("www.google.com")

          self.wait_presence_of_element_located(By.NAME,self.textbox_applicantname_name).send_keys("Applicant name")
          self.wait_presence_of_element_located(By.NAME, self.textbox_applicanttitle_name).send_keys("title")
          self.wait_presence_of_element_located(By.NAME, self.textbox_applicantemail_name).send_keys("abc@gmail.com")
          self.wait_presence_of_element_located(By.NAME, self.textbox_applicantphone_name).send_keys("4545454545")

          self.wait_presence_of_element_located(By.NAME, self.textbox_staffName_name).send_keys("Divya")
          self.wait_presence_of_element_located(By.NAME, self.textbox_staffTitle_name).send_keys("stafftitle")

          self.wait_presence_of_element_located(By.NAME,self.textbox_staffEmail_name).send_keys("dbcham1983@gmail.com")
          self.wait_presence_of_element_located(By.NAME,self.textbox_staffUshjaId_name).send_keys("HJ6002894")

          self.wait_presence_of_element_located(By.XPATH, self.textbox_zone_xpath).send_keys("zone1")
          time.sleep(2)
          self.wait_presence_of_element_located(By.XPATH, self.radio_isCredentializedInstructor_yes_xpath).click()
          status_isCredentialized_yes=self.wait_presence_of_element_located(By.XPATH,self.radio_isCredentializedInstructor_yes_xpath).is_selected()
          if(status_isCredentialized_yes) :
                print("INSIDE IF *************")
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                self.wait_presence_of_element_located(By.NAME,self.textbox_icStaffUshjaId_name).send_keys("HJ6002894")
          else:
               pass
          self.wait_presence_of_element_located(By.XPATH,self.button_facility_xpath).click()
          time.sleep(2)
          ##################  FACILITY ###################

          self.wait_presence_of_element_located(By.XPATH,self.textarea_interest_USHJA_xpath ).send_keys("interests ")
          time.sleep(2)
          self.wait_presence_of_element_located(By.XPATH,self.textarea_academyPrograms_xpath).send_keys("academy program boarding")
          time.sleep(2)
          ### Radio Options start
          isDailyfeedAndFreshwater="Yes"
          if(isDailyfeedAndFreshwater.capitalize()== 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isDailyfeedAndFreshwaterYes_xpath).click()
          elif(isDailyfeedAndFreshwater.capitalize()== 'No'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isDailyfeedAndFreshwaterNo_xpath).click()
          time.sleep(2)

          isWeatherAppropriate="No"
          if(isWeatherAppropriate.capitalize()=='Yes'):
            self.wait_presence_of_element_located(By.XPATH,self.radio_isWeatherAppropriateYes_xpath).click()
          elif(isWeatherAppropriate.capitalize()=='No'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isWeatherAppropriateNo_xpath).click()
          time.sleep(2)

          isRoutineVaterinarian="Yes"
          if(isRoutineVaterinarian.capitalize()=="Yes"):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isRoutineVaterinarianYes_xpath).click()
          elif(isRoutineVaterinarian.capitalize()=="No"):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isRoutineVaterinarianNo_xpath).click()
          time.sleep(2)

          isDailyTurnoutOpportunities='No'
          if(isDailyTurnoutOpportunities.capitalize()=='Yes'):
              self.wait_presence_of_element_located(By.XPATH, self.radio_isDailyTurnoutOpportunitiesYes_xpath).click()
          elif(isDailyTurnoutOpportunities.capitalize()=='No') :
               self.wait_presence_of_element_located(By.XPATH, self.radio_isDailyTurnoutOpportunitiesNo_xpath).click()
          time.sleep(2)

          isDewormingSchedule= 'Yes'
          if(isDewormingSchedule.capitalize()=='Yes'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isDewormingScheduleYes_xpath).click()

          elif(isDewormingSchedule.capitalize()=='No'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isDewormingScheduleNo_xpath).click()
          time.sleep(2)

          isSafeRidingArea='Yes'
          if(isSafeRidingArea.capitalize()=='Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isSafeRidingAreaYes_xpath).click()
          elif(isSafeRidingArea.capitalize()=='No'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isSafeRidingAreaNo_xpath).click()
          time.sleep(2)

          isThereCoveredLocation="Yes"
          if(isThereCoveredLocation.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereCoveredLocationYes_xpath).click()
          elif(isThereCoveredLocation.capitalize() == 'No'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereCoveredLocationNo_xpath).click()
          time.sleep(2)

          isThereRestrooms="temporary"
          if(isThereRestrooms.capitalize()=='Permanent'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereRestroomsPermanent_xpath).click()
          elif(isThereRestrooms.capitalize()=='Temporary'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereRestroomstemporary_xpath).click()
          elif(isThereRestrooms.capitalize() == 'None'):
                self.wait_presence_of_element_located(By.XPATH, self.radio_isThereRestroomsnone_xpath).click()
          time.sleep(3)

          isThereOffice='Yes'
          if(isThereOffice.capitalize() =='Yes'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereofficeYes_xpath).click()
          elif(isThereOffice.capitalize() =='No'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereofficeNo_xpath).click()
          time.sleep(2)

          isThereClassroom="Yes"
          if(isThereClassroom.capitalize()=='Yes'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereClassroomYes_xpath).click()
          elif(isThereClassroom.capitalize()=='No' ):

               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereClassroomNo_xpath).click()
          time.sleep(2)

          areThereLocker="Yes"
          if(areThereLocker.capitalize() == 'Yes') :
               self.wait_presence_of_element_located(By.XPATH, self.radio_areThereLockerYes_xpath).click()
          elif(areThereLocker.capitalize() == 'No') :
               self.wait_presence_of_element_located(By.XPATH, self.radio_areThereLockerNo_xpath).click()
          time.sleep(2)

          isThereAdequateParking="No"
          if(isThereAdequateParking.capitalize()=='Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereAdequateParkingYes_xpath).click()
          elif(isThereAdequateParking.capitalize()=='No'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereAdequateParkingNo_xpath).click()
          time.sleep(2)

          isThereClubroom="No"
          if(isThereClubroom.capitalize()=="Yes"):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereClubroomYes_xpath).click()
          elif(isThereClubroom.capitalize()=="No")   :
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereClubroomNo_xpath).click()
          time.sleep(2)

          isThereInternet="Yes"
          if(isThereInternet.capitalize()=='Yes'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereInternetYes_xpath).click()
          elif(isThereInternet.capitalize()=="No") :
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereClubroomNo_xpath).click()
          time.sleep(2)

          self.wait_presence_of_element_located(By.XPATH, self. button_operational_xpath).click()
          time.sleep(2)


          ############################  3rd form  OPERATIONAL   ###############

          self.wait_presence_of_element_located(By.NAME,self.textbox_noOfParticipants_name).send_keys("facility1")
          self.wait_presence_of_element_located(By.NAME,self.textbox_noOfHunters_name).send_keys("testing")
          self.wait_presence_of_element_located(By.NAME,self.textarea_typesOfLessons_name).send_keys("lessons offered by disciplines")
          areThereInstructionLevel="Yes"
          if(areThereInstructionLevel.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_areThereInstructionLevelYes_xpath).click()
               time.sleep(2)
               self.wait_presence_of_element_located(By.NAME,self.textarea_levelsOfLessons_name).send_keys("Testing done for lessons area")

          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_areThereInstructionLevelNo_xpath).click()

          doesAcademyOfferNonrideInstruction="Yes"
          if(doesAcademyOfferNonrideInstruction.capitalize() =='Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesAcademyOfferNonrideInstructionYes_xpath).click()
               self.wait_presence_of_element_located(By.NAME,self.textarea_academyOfferedNonrideInstruction_name).send_keys("Non ride instructions should be here")
          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesAcademyOfferNonrideInstructionNo_xpath).click()


          self.wait_presence_of_element_located(By.NAME,self.textbox_ratioOfInstructor_name).send_keys("1:10")
          self.wait_presence_of_element_located(By.NAME,self.textbox_noOfSchoolHorses_name).send_keys("2")

          isScheduleDailyBreak = "No"
          if (isScheduleDailyBreak.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH, self.radio_isScheduleDailyBreakYes_xpath).click()
          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_isScheduleDailyBreakNo_xpath).click()

          self.wait_presence_of_element_located(By.XPATH,self.button_services_xpath).click()
          time.sleep(2)

          #################   4th form SERVICES  ################
          doesAcademyOfferSocialServices='Yes'
          if (doesAcademyOfferSocialServices.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesAcademyOfferSocialServicesYes_xpath).click()
               self.wait_presence_of_element_located(By.NAME,self.textarea_academyOfferedSocialServices_name).send_keys("Social services camps")

          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_doesAcademyOfferSocialServicesNo_xpath).click()


          checkbox_name=['IEA','NONE']
          for n in checkbox_name:
             print("value inside loop:",n)

             self.wait_presence_of_element_located(By.XPATH,"//input[contains(@class,'PrivateSwitchBase-input-' ) and  contains(@value,'" + n + "')]").click()

          self.wait_presence_of_element_located(By.NAME,self.textbox_otherAspectsOfAcademyOperation_name).send_keys("RYTRTYRY")
          self.wait_presence_of_element_located(By.XPATH, self.button_safety_xpath).click()
          time.sleep(4)

          ###########################  5th FORM  SAFETY  ################################
          areRequireToWearHelmet="Yes"
          if(areRequireToWearHelmet.capitalize() == "Yes"):
                 self.wait_presence_of_element_located(By.XPATH,self.radio_areRequireToWearHelmetYes_xpath).click()

          else:
                 self.wait_presence_of_element_located(By.XPATH,self.radio_areRequireToWearHelmetNo_xpath).click()

          doesRequireToSignReleaseOfLiability="No"
          if(doesRequireToSignReleaseOfLiability.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesRequireToSignReleaseOfLiabilityYes_xpath).click()
          else:

               self.wait_presence_of_element_located(By.XPATH,self.radio_doesRequireToSignReleaseOfLiabilityNo_xpath).click()

          time.sleep(2)
          doesAcademyCarryInsurance="Yes"
          if(doesAcademyCarryInsurance == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesAcademyCarryInsuranceYes_xpath).click()
               time.sleep(4)
               choosefile=self.wait_presence_of_element_located(By.XPATH,self. button_choosefilelocate_xpath)
               self.driver.execute_script("arguments[0].scrollIntoView();", choosefile)
               time.sleep(4)
               choose_file_insurance= self.wait_presence_of_element_located(By.XPATH,"//span[contains(text(),'Choose File')]//ancestor::div/input[@type='file']")
               choose_file_insurance.send_keys("C:\\Users\\Admin\\Desktop\\upload.txt")
               time.sleep(4)


          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_doesAcademyCarryInsuranceNo_xpath).click()

          isThereSafetyPlan = "No"
          if(isThereSafetyPlan.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereSafetyPlanYes_xpath).click()
          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereSafetyPlanNo_xpath).click()

          isTelephoneAvailable ='Yes'
          if(isTelephoneAvailable.capitalize() =='Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isTelephoneAvailableYes_xpath).click()
          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_isTelephoneAvailableNo_xpath).click()

          isStocked ='Yes'
          if( isStocked == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isStockedYes_xpath).click()
          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_isStockedNo_xpath).click()

          isThereStaffFamiliarWithCpr = "Yes"
          if(isThereStaffFamiliarWithCpr  == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereStaffFamiliarWithCprYes_xpath).click()
               self.wait_presence_of_element_located(By.NAME,self.textarea_staffName_name).send_keys("testing staff name")

          else:
               self.wait_presence_of_element_located(By.XPATH, self.radio_isThereStaffFamiliarWithCprNo_xpath).click()

          self.wait_presence_of_element_located(By.XPATH,self.button_Miscellaneous_xpath).click()

          ######################   6th form MISCELLANEOUS ##################
          time.sleep(2)
          areThereMinStandardsForInstructor='Yes'
          if(areThereMinStandardsForInstructor.capitalize() == 'Yes' ):
               self.wait_presence_of_element_located(By.XPATH,self.radio_areThereMinStandardsForInstructorYes_xpath).click()
               time.sleep(2)
               self.wait_presence_of_element_located(By.XPATH,self.textarea_StandardsForInstructor_xpath).send_keys("standards for an instructor")
          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_areThereMinStandardsForInstructorNo_xpath).click()

          time.sleep(4)
          isThereOpportunityForCareerDevelopment = 'Yes'
          if(isThereOpportunityForCareerDevelopment.capitalize() == 'Yes'):
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereOpportunityForCareerDevelopmentYes_xpath).click()
               time.sleep(2)
               self.wait_presence_of_element_located(By.XPATH,self.textarea_opportunityForCareerDevelopment_xpath).send_keys("Testing")

          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_isThereOpportunityForCareerDevelopmentNo_xpath).click()

          time.sleep(2)
          radio_doesAcademyAdvertiseForNewStudents = 'Yes'
          if(radio_doesAcademyAdvertiseForNewStudents.capitalize() == 'Yes') :
               self.wait_presence_of_element_located(By.XPATH, self.radio_doesAcademyAdvertiseForNewStudentsYes_xpath).click()
               time.sleep(2)
               self.wait_presence_of_element_located(By.XPATH,self.textarea_howAcademyAdvertiseForNewStudents_xpath).send_keys("AcademyAdvertiseForNewStudents")

          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_doesAcademyAdvertiseForNewStudentsNo_xpath).click()

          time.sleep(2)
          radio_isAcademyWillingToWorkWithUshja= 'Yes'
          if(radio_isAcademyWillingToWorkWithUshja.capitalize() == 'Yes'):
                self.wait_presence_of_element_located(By.XPATH, self.radio_isAcademyWillingToWorkWithUshjaYes_xpath).click()

          else:
               self.wait_presence_of_element_located(By.XPATH,self.radio_isAcademyWillingToWorkWithUshjaNo_xpath).click()

          time.sleep(2)
          self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
          time.sleep(20)
          more_info=["Horsemanship Quiz","Instructor Credential"]
          for info in more_info:
               print("INFO:",info)
               self.wait_presence_of_element_located(By.XPATH,"//div/label[@class='MuiFormControlLabel-root']//child::span/input[@name='interestOfParticipation']//ancestor::span//following-sibling::span/p[contains(text(),'" + info + "')]").click()
               time.sleep(2)

          self.wait_presence_of_element_located(By.XPATH,self.button_reference_xpath).click()
          time.sleep(2)

          self.wait_presence_of_element_located(By.XPATH,self.textbox_referencename_xpath).send_keys("name")

         ###################  7th form REFERENCE ##############

          self.wait_presence_of_element_located(By.NAME,self.textarea_howToHearRRAProgram_name).send_keys("ToHearRRAProgram")


     def alertRRA_present(self):

          try:

               self.wait_presence_of_element_located(By.XPATH, self.text_alertskip_xpath).click()
               self.rra_registration()

          except TimeoutException:

               print("Time out exception")
               self.rra_registration()

          # else:
          #      self.rra_registration()
