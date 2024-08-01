from selenium.webdriver.common.by import By
from selenium import webdriver


class login_page_two():

    def __init__(self,driver):
        self.driver=driver

    user_logged_in=(By.XPATH,"//strong[normalize-space()='CURA Healthcare Service']")


    def get_user_logged_in(self):
        return self.driver.find_elements(*login_page_two.user_logged_in)

    def get_logged_in_text(self):
        return self.get_user_logged_in().text()
