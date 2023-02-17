from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseFunc():
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_of_element_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.presence_of_element_located((id_type, ele_id)))

    def wait_presence_of_all_elements_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 80)
        return wait.until(EC.presence_of_all_elements_located((id_type, ele_id)))
