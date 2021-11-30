# Used to import the webdriver from selenium
from selenium import webdriver
import time
import sys
import glob
import pyautogui
import pygetwindow
from PIL import Image
import datetime
import os


# Get the path of chromedriver which you have install

def startBot(username, password, url, path):

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website in chrome.
    driver.get(url)
    print("Reached Trojan Check")
    driver.implicitly_wait(5)
    # time.sleep(2)

    driver.find_element_by_class_name("button-wrapper").click()
    driver.implicitly_wait(5)
    # time.sleep(3)
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name("j_username").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name("j_password").send_keys(password)
    driver.implicitly_wait(5)
    # time.sleep(3)

    #Process to start assessment
    #driver.find_element_by_name("_eventId_proceed").click()
    #time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.submit-button.btn-next.mat-button.mat-button-base.mat-accent").click()
    driver.implicitly_wait(5)
    # time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.mat-flat-button.mat-button-base.btn-begin-assessment").click()
    driver.implicitly_wait(5)
    # time.sleep(3)
    driver.find_element_by_class_name("mat-focus-indicator.btn-assessment-start.mat-flat-button.mat-button-base").click()
    driver.implicitly_wait(5)
    # time.sleep(3)

    #No and no questions, then next
    driver.find_element_by_id("mat-button-toggle-3").click()
    driver.find_element_by_id("mat-button-toggle-5").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-next.mat-flat-button.mat-button-base").click()

    #Last page of No's
    driver.implicitly_wait(5)
    # time.sleep(3)
    driver.find_element_by_id("mat-button-toggle-14").click()
    driver.find_element_by_id("mat-button-toggle-16").click()
    driver.find_element_by_id("mat-button-toggle-18").click()
    driver.find_element_by_id("mat-button-toggle-20").click()
    driver.find_element_by_id("mat-button-toggle-22").click()
    driver.find_element_by_id("mat-button-toggle-24").click()
    driver.find_element_by_id("mat-button-toggle-26").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-next.mat-flat-button.mat-button-base").click()

    #Verify responses
    driver.implicitly_wait(5)
    # time.sleep(3)
    driver.find_element_by_class_name("mat-checkbox-inner-container").click()
    driver.find_element_by_class_name("mat-focus-indicator.btn-submit.mat-flat-button.mat-button-base").click()

    #Snap a screenshot of the Trojan Check and save to file
    ss_path = "C:\\Dev\\PythonPictures\\Trojan_Check_" + (str(datetime.datetime.now()).split(" "))[0] + ".png"

    window = pygetwindow.getWindowsWithTitle('Trojan Check - Google Chrome')[0]
    # print(window)
    x1 = window.left
    y1 = window.top
    height = window.height
    width = window.width

    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(ss_path)

    im = Image.open(ss_path)
    im = im.crop((x1, y1, x2, y2))
    im.save(ss_path)
    im.show(ss_path)
    while (True):
      pass

# Driver Code
# Enter below your login credentials
f = open("logininfo.txt", "r")
username = f.readline()
password = f.readline()
path = f.readline()

# URL of the login page of site
# which you want to automate login.
url = "https://trojancheck.usc.edu/login"

# Call the function
# Currently working on only calling the function at 12AM (incomplete)
# while True:
#     now = datetime.datetime.now()
#     now_split = str(now).split(" ")
#     date = str(now_split[0])
#     raw_time = str(now_split[1]).split(".")
#     time = str(raw_time[0])

startBot(username, password, url, path)
