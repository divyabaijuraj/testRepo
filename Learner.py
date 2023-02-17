import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utilities.base_class import BaseFunc


class Learner(BaseFunc):


    learner_xpath = "//*[@id='root']/div/nav/div[2]/div/div/div[2]/ul/div[2]/div[2]/span"
    dashboard_xpath="//*[@id='root']/div/nav/div[2]/div/div/div[2]/ul/div[1]/div[2]/span"
    coach_xpath="//*[@id='root']/div/nav/div[2]/div/div/div[2]/ul/div[3]/div[2]/span"

    # learner_xpath="//div[@class='MuiDrawer-root MuiDrawer-docked jss32']/div/div/ul/div[@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button Mui-selected']/div[2]/span[@class='MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock']"
    def __init__(self,driver):
        self.driver=driver


    def dashboard_click(self):
            print(self.driver.title)
            print("OK.....reached!!!!!!!!!!!!!!")


            actions = ActionChains(self.driver)
            coach=self.wait_presence_of_element_located(By.XPATH, self.coach_xpath)
            self.driver.execute_script("arguments[0].click();", coach)
            time.sleep(4)
            # actions.move_to_element(learner).click().perform()



