import time

from selenium.webdriver.common.by import By

from pageObject.Learner import Learner
from utilities.base_class import BaseFunc
from utilities.readProperties import ReadConfig


class LoginUSHJA(BaseFunc):

    textbox_username_xpath="//input[@type='text']"
    textbox_password_xpath="//input[@type='password']"

    button_login_xpath="//button[@type='submit']"
    button_logout_xpath="//button[@class='MuiButtonBase-root MuiIconButton-root']"
    button_logout1_xpath="//*[@d='M7 10l5 5 5-5z']//ancestor::button[@class='MuiButtonBase-root MuiIconButton-root']"
    alert_yes_xpath="//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textSecondary']"



    def __init__(self, driver):

        self.driver = driver
        # self.baseURL = ReadConfig.getApplicationURL()
        # self.username = ReadConfig.getUseremail()
        # self.password = ReadConfig.getPassword()


    #def _init_(self, driver):
           # super()._init_(driver)
            #self.driver = driver

    def setUserName(self,username):
        try:

            return self.wait_presence_of_element_located(By.XPATH,self.textbox_username_xpath).send_keys(username)
        except:
            print("Enter valid Username")

    def setPassword(self,password):
        try:

            self.wait_presence_of_element_located(By.XPATH, self.textbox_password_xpath).clear()
            return self.wait_presence_of_element_located(By.XPATH, self.textbox_password_xpath).send_keys(password)
        except:
            print("Enter valid Password")

    def clickLogin(self):

        return self.wait_presence_of_element_located(By.XPATH, self.button_login_xpath).click()


    def login_page_credentials(self,Username, Password, URL):

        self.driver.get(URL)

        #self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.setUserName(Username)
        self.setPassword(Password)

        self.clickLogin()

    def Logout(self):
        self.wait_presence_of_element_located(By.XPATH,self.button_logout_xpath).click()
        time.sleep(10)
        self.wait_presence_of_element_located(By.XPATH,self.button_logout1_xpath).click()
        time.sleep(10)
        print("OK")
        self.wait_presence_of_element_located(By.XPATH,self.alert_yes_xpath).click()
        time.sleep(6)
        print("OK Done")



