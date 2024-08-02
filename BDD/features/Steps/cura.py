import time

from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By


@given('I am on page called Cura')
def step_implementation(context):
    context.browser=webdriver.Chrome()
    # context.driver=webdriver.Chrome() is also fine
    context.browser.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")

@when('Entering the {Email} and {pwd}')
def step_implementation(context,Email,pwd):
    search_box0= context.browser.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    search_box0.click()
    search_box=context.browser.find_element(By.ID,"txt-username")
    search_box.send_keys(Email)
    search_box2=context.browser.find_element(By.ID,"txt-password")
    search_box2.send_keys(pwd)
    submit_box=context.browser.find_element(By.XPATH,"//button[@id='btn-login']")
    submit_box.click()

@then('I got {output}')
def step_implementation(context,output):
    error_message=context.browser.find_element(By.XPATH,"//p[@class='lead text-danger']")
    assert output in error_message.text
    time.sleep(2)
    context.browser.quit()