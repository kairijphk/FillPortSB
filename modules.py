import time as t
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import cv2
except:
    print('Error importing cv2! Installing fallback!')
    os.system('python -m pip install opencv-python-headless pip')
try:
    import pytesseract
except:
    os.system('python -m pip install pytesseract pip')
    os.system('python -m pip install tesseract-ocr pip')
    os.system('python -m pip install libtesseract-dev pip')
def loader():
    pytesseract.pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'
def search(text,list):
    for x in list:
        if x == text:
            found = True
            print('Skipping Tutorial...')
            return True
    print('Rescanning...')
def getimage(driver):
    driver.get_screenshot_as_file('imagescrape\\Starbreak.png') 
    img = cv2.imread('imagescrape\\Starbreak.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, None, fx=2, fy=2)
    output = pytesseract.image_to_string(img)
    output = output.lower()
    return output
def register(driver):
    global found
    found = False
    while found == False:
        output = getimage(driver)
        print(output)
        output2 = output.split(' ')
        print(output2)
        if search('signed',output2) == True:
                found = True
        else:
            if search('uswest',output2) == True:
                    found = True
                    break
            else:
                if search('as:',output2) == True:
                    found = True
                    break
                else: 
                    if search('server:',output2) == True:
                        found = True
                        break
        t.sleep(0.5)
    ActionChains(driver)\
        .send_keys(Keys.ENTER)\
        .perform()
    found = False
    while found == False:
        index = 0
        while index < 10:
            driver.get_screenshot_as_file('imagescrape\\Starbreak.png') 
            img = cv2.imread('imagescrape\\Starbreak.png')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, None, fx=2, fy=2)
            index += 1
            output = pytesseract.image_to_string(img)
            output = output.lower()
            print(output)
            output2 = output.split(' ')
            print(output2)
            if search('tutorial',output2) == True:
                found = True
            else:
                if search('[h]',output2) == True:
                    found = True
                    break
                else:
                    if search('skip',output2) == True:
                        found = True
                        break
                    else: 
                        if search('portal',output2) == True:
                            found = True
                            break
                        else: 
                            if search('elite',output2) == True:
                                found = True
                                break
        t.sleep(0.5)
    for i in range(10):
        ActionChains(driver)\
            .send_keys("[")\
            .perform()
        ActionChains(driver)\
            .send_keys("m")\
            .send_keys("n")\
            .perform()
        ActionChains(driver)\
            .send_keys("H")\
            .perform()
    print('a')
def fillSC(driver):
    global action_key_down_RIGHT, action_key_up_RIGHT, action_key_down_UP, action_key_up_UP
    action_key_down_RIGHT = ActionChains(driver).key_down(Keys.ARROW_RIGHT)
    action_key_up_RIGHT= ActionChains(driver).key_up(Keys.ARROW_RIGHT)
    action_key_down_UP = ActionChains(driver).key_down(Keys.SPACE)
    action_key_up_UP = ActionChains(driver).key_up(Keys.SPACE)
    action_key_down_LEFT = ActionChains(driver).key_down(Keys.ARROW_LEFT)
    action_key_up_LEFT = ActionChains(driver).key_up(Keys.ARROW_LEFT)
    t.sleep(1)
    performkeys(action_key_up_RIGHT,action_key_down_RIGHT,1.9)
    performkeys(action_key_up_UP,action_key_down_UP,1)
    performkeys(action_key_up_LEFT,action_key_down_LEFT,0.125)
    t.sleep(0.5)
    ActionChains(driver)\
            .send_keys("A")\
            .perform()

def performkeys(keyup,keydown,delay):
    endtime = t.time() + delay
    while True:
        keydown.perform()

        if t.time() > endtime:
            keyup.perform()
            break
#2.5 
#0.75
#A