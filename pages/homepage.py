class LogOut:
    def __init__(self,driver):
        self.driver=driver
        self.logout_link="//a[text()='Logout']"
    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link).click()
        self.driver.close()