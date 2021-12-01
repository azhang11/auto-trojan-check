# Screenshot QR Code (move into function after completion)
import pygetwindow
import pyautogui
from PIL import Image
import datetime

#'Trojan Check - Google Chrome'
ss_name = "screenshot"
ss_path = "C:\\Dev\\PythonPictures\\Trojan_Check_" + (str(datetime.datetime.now()).split(" "))[0] + ".png"

window = pygetwindow.getWindowsWithTitle('Trojan Check - Google Chrome')[0]
#print(window)
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