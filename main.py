# C:\Users\andre\Downloads\chromedriver_win32 (1)
# https://www.stealmylogin.com/demo.html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import requests

url = "https://www.goldmansachs.com/"
username = "tomsmith"
password = "SuperSecretPassword!"

#options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option("useAutomationExtension", False)

service = ChromeService(executable_path="C:\\Dev\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)
while (True):
    pass
print(driver.title)

#driver.find_element("username").send_keys(username)
#driver.find_element("password").send_keys(password)
#login_button = driver.find_element("submit")
#login_button.submit()
