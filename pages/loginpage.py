from utils.constants import *
from pages.webgeneric import WebGeneric

class Loginpage(WebGeneric):
    def __init__(self,driver):
        # self.driver=driver
        WebGeneric.__init__(self, driver)
        global wg
        wg=WebGeneric(driver)
        #locators identified by name
        self.UN='username'
        self.PWD='pwd'
        self.submit_xpath="//div[text()='Login ']"

    def enter_user_name(self):
        # self.driver.find_element_by_name(self.UN).send_keys(USER_NAME)
        wg.enter(self.UN,USER_NAME)

    def enter_password(self):
        # self.driver.find_element_by_name(self.PWD).send_keys(PASSWORD)
        wg.enter(self.PWD,PASSWORD)

    def click_submit(self):
        # self.driver.find_element_by_xpath(self.submit_xpath).click()
        wg.click_btn(self.submit_xpath)