from selenium import webdriver
import os
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

journey = browser.find_element_by_css_selector('.btn')
journey.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(calc(x))

button = browser.find_element_by_css_selector('.btn')
button.click()