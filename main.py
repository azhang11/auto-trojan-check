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

    #Process to start assessment
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.submit-button.btn-next.mat-button.mat-button-base.mat-accent").click()
    time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.mat-flat-button.mat-button-base.btn-begin-assessment").click()
    time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.btn-assessment-start.mat-flat-button.mat-button-base").click()
    time.sleep(3)

    #No and no questions, then next
    driver.find_element_by_id("mat-button-toggle-3").click()
    driver.find_element_by_id("mat-button-toggle-5").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-next.mat-flat-button.mat-button-base").click()

    #Last page of No's
    time.sleep(3)
    driver.find_element_by_id("mat-button-toggle-14").click()
    driver.find_element_by_id("mat-button-toggle-16").click()
    driver.find_element_by_id("mat-button-toggle-18").click()
    driver.find_element_by_id("mat-button-toggle-20").click()
    driver.find_element_by_id("mat-button-toggle-22").click()
    driver.find_element_by_id("mat-button-toggle-24").click()
    driver.find_element_by_id("mat-button-toggle-26").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-next.mat-flat-button.mat-button-base").click()

    #Verify responses
    time.sleep(3)
    driver.find_element_by_class_name("mat-checkbox-inner-container").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-submit.mat-flat-button.mat-button-base").click()
    while (True):
      pass

# Driver Code
# Enter below your login credentials
f = open("logininfo.txt", "r")
username = f.readline()
password = f.readline()

# URL of the login page of site
# which you want to automate login.
url = "https://trojancheck.usc.edu/login"
# Call the function
startBot(username, password, url)