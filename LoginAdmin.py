import time

from selenium.webdriver.common.by import By

from pageObject.Learner import Learner
from utilities.base_class import BaseFunc
from utilities.readProperties import ReadConfig


class LoginAdminUSHJA(BaseFunc):
    textbox_username_xpath="//input[@name='username'  and @type='text']"
    textbox_password_xpath="//input[@name='password'  and @type='password']"
    button_login_xpath="//button[@type='submit']"

    def __init__(self, driver):

        self.driver = driver
        self. baseURL = ReadConfig.getadminURL()
        self.username = ReadConfig.getAdminUser()
        self.password = ReadConfig.getAdminPassword()

    def setUserName(self, username):
        try:

            return self.wait_presence_of_element_located(By.XPATH, self.textbox_username_xpath).send_keys(username)
        except:
            print("Enter valid Username")

    def setPassword(self, password):
        try:

            self.wait_presence_of_element_located(By.XPATH, self.textbox_password_xpath).clear()
            return self.wait_presence_of_element_located(By.XPATH, self.textbox_password_xpath).send_keys(password)
        except:
            print("Enter valid Password")

    def clickLogin(self):

        return self.wait_presence_of_element_located(By.XPATH, self.button_login_xpath).click()

    def login_page_credentials(self,username,password,login_url):


        # self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        # self.setUserName(self.username)
        # self.setPassword(self.password)
        # self.clickLogin()
        self.driver.get(login_url)

        self.driver.maximize_window()
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()

