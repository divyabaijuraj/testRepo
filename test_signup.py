import time

import pytest
import softest
from utilities.customeLogger import LogGen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.LoginPage import LoginUSHJA
from ddt import ddt, data, unpack
from pageObject.SignUp import SignUp

from utilities.utils import Utilities

@ddt
class TestSignUp(softest.TestCase):
    logger = LogGen.loggen()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.signup=SignUp(self.driver)
        self.logger = LogGen.loggen()

    @data(*Utilities.read_data_from_excel("C:\\Users\\Admin\\PycharmProjects\\USHJA\\TestData\\USHJADATA.xlsx", "Sheet2"))
    @unpack
    def test_signup(self,URL,AccountType,Username,Password,ConfirmPassword,OrganizationName,Address1,Address2,City,Country,State,Zip,PhoneCountry,Phone,Email):
        print(URL)
        self.signup.sign_up(URL,AccountType,Username,Password,ConfirmPassword,OrganizationName,Address1,Address2,City,Country,State,Zip,PhoneCountry,Phone,Email)





