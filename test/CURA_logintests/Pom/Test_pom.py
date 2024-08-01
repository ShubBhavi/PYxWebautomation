import pytest
from selenium import webdriver
from test.pageobjects.loginpage import Login_page
from dotenv import load_dotenv
import os




class Test_Login():

    @pytest.mark.usefixtures("setup")
    def test_positive1(self,setup):
        driver = setup
        driver.get(self.url)
        login_page = Login_page(driver)
        login_page.get_makeappointment()
        login_page.login_to_cura(user=self.name, pwd=self.password)
        url = driver.current_url
        print(url)
        assert url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    @pytest.mark.usefixtures("setup")
    def test_negative1(self,setup):
        driver = setup
        login_page = Login_page(driver)
        login_page.get_makeappointment()
        login_page.login_to_cura(user="admin", pwd="admin")
        Error = login_page.Error_message()
        assert Error == "Login failed! Please ensure the username and password are valid."
