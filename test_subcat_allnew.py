import softest

from pageObjects.LoginPage import LoginPage
from pageObjects.SubCategory import SubCategory
from pageObjects.SubCategoryEdit import SubCategoryEdit
from pageObjects.SubCategoryDelete import SubCategoryDelete
from utilities.customLogger import LogGen

from ddt import ddt, data, unpack
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.utils import Utilities


@ddt
class TestSubcatAlberta(softest.TestCase):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utilities()
        self.lp=LoginPage(self.driver)
        self.sub=SubCategory(self.driver)
        self.subedit=SubCategoryEdit(self.driver)
        self.subdel=SubCategoryDelete(self.driver)

    ##############  Login

    @data(*Utilities.read_data_from_excel("D:\\backup 25-7-22\\PycharmProjects\\pythonProject\\alberta\\TestData\\SUBCAT.xlsx", "login"))
    #@data(('harikt@gmail.com', '123456', 'https://testcustomer.albertapayments.com/login'))
    @unpack
    def test_login_ddt(self, username, password,URL):
        logger = LogGen.loggen()
        print(username, password)
        self.lp.login_page_credentials(username, password,URL)
        if(self.driver.title == 'Customer-Alberta | Dashboard'):
             logger.info("Logged in to Alberta")

        else:
            logger.info("Error occured")

    ##### subcategory add

    @data(*Utilities.read_data_from_excel("D:\\backup 25-7-22\\PycharmProjects\\pythonProject\\alberta\\TestData\\SUBCAT.xlsx", "Sheet1"))
    @unpack

    def test_subcatadd(self, Name, Category):
        print(Name,"inside function")
        self.sub.addsubCategory(Name,Category)


    ############## Subcategory Delete
    @data(*Utilities.read_data_from_excel("D:\\backup 25-7-22\\PycharmProjects\\pythonProject\\alberta\\TestData\\SUBCAT.xlsx", "Delete"))
    @unpack
    def test_subcatdelete(self, Name):
        self.subdel.inventory_subcategoryClick()
        self.subdel.search_deletename(Name)
        self.driver.back()



'''
    ######  Subcategory Edit
    @data(*Utilities.read_data_from_excel("D:\\backup 25-7-22\\PycharmProjects\\pythonProject\\alberta\\TestData\\SUBCAT.xlsx", "Edit"))
    @unpack
    def test_subcatedit(self, Name, Category, Name_edit):

        self.subedit.inventory_subcategoryClick()
        self.subedit.edit_Subcat_name(Name, Category, Name_edit)
'''