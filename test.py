import time as t
import random
import modules
import subprocess
try:
    from selenium import webdriver
except:
    print('Could not find Selenium, attempting to install...')
    shellscript = subprocess.Popen(["setup.sh"], stdin=subprocess.PIPE)
try:
    from selenium import webdriver
except:
    print('ERROR! Program WILL ERROR. Selenium NOT FOUND.')
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
print('Running SC Filler v1.0.1 Public Release')
driver = webdriver.Edge()
driver.get('https://www.starbreak.com/')
# Open the website in a web browser
#functions
modules.loader()
modules.register(driver)
modules.fillSC(driver)
input("end?")
