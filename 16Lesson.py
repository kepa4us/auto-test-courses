from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(12)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

book = browser.find_element_by_css_selector('#book')
book.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(calc(x))

button = browser.find_element_by_css_selector('#solve')
button.click()