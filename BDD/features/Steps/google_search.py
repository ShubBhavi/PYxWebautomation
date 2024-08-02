import time

from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By


@given('I am on the google page')
def step_implementation(context):
    context.browser=webdriver.Chrome()
    # context.driver=webdriver.Chrome() is also fine
    context.browser.get("https://www.google.co.in/")

@when('I search for "{search_term}"')
def step_implementation(context,search_term):
    search_box=context.browser.find_element(By.XPATH,"//textarea[@id='APjFqb']")
    search_box.send_keys(search_term)
    search_box.submit()

@then('I should see the "{expected_term}" in the result')
def step_implementation(context,expected_term):
    assert expected_term in context.browser.page_source
    time.sleep(5)

