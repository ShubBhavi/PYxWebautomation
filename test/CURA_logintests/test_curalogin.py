import time

import pytest
from selenium import webdriver
from test.pageobjects.loginpage import Login_page

@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    return driver


def test_positive1(setup):
    driver=setup
    login_page=Login_page(driver)
    login_page.get_makeappointment()
    login_page.login_to_cura(user="John Doe",pwd="ThisIsNotAPassword")
    url=driver.current_url
    print(url)
    assert url=="https://katalon-demo-cura.herokuapp.com/#appointment"

def test_negative1(setup):
    driver=setup
    login_page=Login_page(driver)
    login_page.get_makeappointment()
    login_page.login_to_cura(user="admin",pwd="admin")
    Error=login_page.Error_message()
    assert Error=="Login failed! Please ensure the username and password are valid."

