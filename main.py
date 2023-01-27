'''
RUN THIS FILE!
'''
import os
try:
    from selenium import webdriver
except:
    print('Could not find Selenium, attempting to install...')
    os.system('python -m pip install selenium pip')
    print('Installed Selenium')
try:
    import cv2
except:
    os.system('python -m pip install ffmpeg pip')
    os.system('python -m pip install opencv-python pip')

print('''
░██████╗░█████╗░  ███████╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝  █████╗░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
░╚═══██╗██║░░██╗  ██╔══╝░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝  ██║░░░░░██║███████╗███████╗███████╗██║░░██║
╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')
try:
    from selenium import webdriver
except:
    print('ERROR! Program WILL ERROR. Selenium NOT FOUND.')
import time as t
import random
import modules
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
driver1 = webdriver.Edge(r"msedgedriver.exe")
t.sleep(0.5)
driver1.get('https://www.starbreak.com/')
# Open the website in a web browser
#functions
modules.loader()
modules.register(driver1)
modules.fillSC(driver1)
