from selenium import webdriver
from utils.constants import *
from pages.loginpage import Loginpage
from pages.homepage import LogOut
from pages.webgeneric import WebGeneric
import time
import pytest

@pytest.mark.usefixtures("test_set_up")
class TestLogin:
    def test_login(self):
        driver=self.driver
        lp=Loginpage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_submit()

    def test_logout(self):
        driver = self.driver
        hp=LogOut(driver)
        time.sleep(5)
        hp.click_logout()