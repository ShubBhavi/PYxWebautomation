# page class
# page locators
# page actions
# webdriver _init_
# custom functions
# no assertions here


from selenium.webdriver.common.by import By
from selenium import webdriver

class Login_page():

    def __init__(self, driver):
        self.driver = driver


    # page locatore
    make_appointment=(By.XPATH,"//a[@id='btn-make-appointment']")
    username=(By.XPATH,"//input[@id='txt-username']")
    password=(By.CSS_SELECTOR,"//input[@id='txt-password']")
    login_button=(By.XPATH,"//button[@id='btn-login']")


    # return Webelements

    def get_makeappointment(self):
        return self.driver.find_element(*Login_page.make_appointment)
    def get_username(self):
        return self.driver.find_element(*Login_page.username)

    def get_password(self):
        return self.driver.find_element(*Login_page.password)

    def get_login_button(self):
        return self.driver.find_element(*Login_page.login_button)


    def login_to_cura(self,user,pwd):
        self.get_makeappointment().click()
        self.get_username().send_keys(user)
        self.get_username().send_keys(pwd)
        self.get_login_button().click()













