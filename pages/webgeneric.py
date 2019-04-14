class WebGeneric:
    def __init__(self,driver):
        self.driver=driver

    def enter(self,locator,input_val):
        self.driver.find_element_by_name(locator).send_keys(input_val)

    def click_btn(self,locator):
        self.driver.find_element_by_xpath(locator).click()