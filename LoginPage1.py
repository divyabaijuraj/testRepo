import time

from selenium.webdriver.common.by import By

from pageObject.Learner import Learner
from utilities.base_class import BaseFunc


class LoginiBridge360(BaseFunc):
    link_sign_in_xpath="//a[@class='jss4'  and @href='/sign-in']"
    username_textbox_id='email'
    password_textbox_id="password"

    button_login_xpath="//button[@type='submit']"



    def __init__(self,driver):
        self.driver=driver


    def login(self, username, password):
          self.wait_presence_of_element_located(By.XPATH, self.link_sign_in_xpath).click()
          time.sleep(4)
          self.wait_presence_of_element_located(By.ID, self.username_textbox_id).send_keys(username)
          self.wait_presence_of_element_located(By.ID, self.password_textbox_id).send_keys(password)
          self.wait_presence_of_element_located(By.XPATH, self.button_login_xpath).click()

    # else:
      #       self.wait_presence_of_element_located(By.XPATH, "// a[contains(text(), 'Sign Up')]").click()
      #
      #





    def login_iBridge(self,username,password):
        #self.driver.get(URL)
        self.driver.maximize_window()

        self.login(username,password)
