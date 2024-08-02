import time

from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By


@given('I am on the app vo home page')
def step_implementation(context):
    context.browser=webdriver.Chrome()
    # context.driver=webdriver.Chrome() is also fine
    context.browser.get("https://app.vwo.com/#/login")

@when('I enter the value for {username} and {password}')
def step_implementation(context,username,password):
    search_box=context.browser.find_element(By.XPATH,"//input[@id='login-username']")
    search_box.send_keys(username)
    search_box2=context.browser.find_element(By.XPATH,"//input[@id='login-password']")
    search_box2.send_keys(password)
    submit_box=context.browser.find_element(By.XPATH,"//button[@id='js-login-btn']")
    submit_box.click()

@then('I get the {message}')
def step_implementation(context,message):
    # error_message=context.browser.find_element(By.XPATH,"//div[@id='js-notification-box-msg']")
    # assert message in error_message.txt()
    print(message)
    time.sleep(2)
    context.browser.quit()