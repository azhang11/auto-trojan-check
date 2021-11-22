# Used to import the webdriver from selenium
from selenium import webdriver
import time
import os


# Get the path of chromedriver which you have install

def startBot(username, password, url):
    path = "C:\\Dev\\WebDrivers\\chromedriver.exe"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website in chrome.
    driver.get(url)
    # driver.implicitly_wait(20000)
    time.sleep(2)

    driver.find_element_by_class_name("button-wrapper").click()
    time.sleep(3)
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name("j_username").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name("j_password").send_keys(password)

    # click on submit
    # driver.find_element_by_css_selector("_eventId_proceed").click()
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.submit-button.btn-next.mat-button.mat-button-base.mat-accent").click()
    while (True):
      pass

# Driver Code
# Enter below your login credentials
username = "azhang65"
password = "#Vcs6924@Vcs6924"

# URL of the login page of site
# which you want to automate login.
url = "https://trojancheck.usc.edu/login"
# Call the function
startBot(username, password, url)