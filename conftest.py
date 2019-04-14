import pytest
from utils.constants import *
from selenium import webdriver

# def test_launch():
#     global driver
#     driver=webdriver.Chrome(executable_path="C:/Users/Satish/PycharmProjects/Newsetup/drivers/chromedriver.exe")
#     driver.get(URL)
#     driver.implicitly_wait(40)
#     driver.maximize_window()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in your browser Name e.g chrome, Firefox")

@pytest.fixture(scope='class')
def test_set_up(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:/Users/Satish/PycharmProjects/Automatio_POM_framework/drivers/chromedriver.exe")
    elif browser == "ff":
        driver = webdriver.Firefox(
            executable_path="C:/Users/Satish/PycharmProjects/Automatio_POM_framework/drivers/geckodriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()