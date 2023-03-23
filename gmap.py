from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# for screenshot processing
from PIL import Image
from io import BytesIO

import urllib.request
import time

import os

# COORDINATE_LIST = ["27.993429, -82.539323", "27.993422, -82.540487", "27.993467, -82.541958"]
COORDINATE_LIST = ["39.895574, -104.694017"]

# ORLANDO
# "28.448891, -81.320172"

# FT LAUDER DALE
# "27.983583, -82.528116"

# SIKORSKY
# 41.255588, -73.089107

# MIAMI
# 25.799118, -80.291341
# 25.802977, -80.299560

# KENNEDY SPACE CENTER
# 28.595725, -80.679871

# DENVER
# 39.895574, -104.694017







# Worker that runs a screenshot and a navigation
def worker(driver, starting_coordinates):

    # # search for the location you want to download a satellite image for
    search_box = driver.find_element(by=By.XPATH, value="//input[@id='searchboxinput']")
    search_box.send_keys(starting_coordinates) 
    search_button = driver.find_element(by=By.XPATH, value="//button[@id='searchbox-searchbutton']")
    search_button.click()
    time.sleep(2) # wait to load
    collapse_button = driver.find_element(by=By.XPATH, value="//button[@class='yra0jd Hk4XGb']")
    collapse_button.click()
    time.sleep(1) # wait to react

    # switch to satellite view
    satellite_button = driver.find_element(by=By.XPATH, value="//button[@class='yHc72 qk5Wte']")
    satellite_button.click()

    time.sleep(2) # wait to load

    # zoom in to the desired level
    for i in range(5):
        zoom_in_button = driver.find_element(by=By.XPATH, value="//button[@id='widget-zoom-in']")
        zoom_in_button.click()
        time.sleep(.75)

    for i in range(100):
        run_screenshot(driver, i, starting_coordinates)

    # close the driver
    driver.quit()

# takes screenshot and moves down
def run_screenshot(driver, itr, starting_coordinates):
    # take a screenshot
    img_name=starting_coordinates +'_ss' + str(itr) + '.png'
    driver.save_screenshot(img_name)
    im = Image.open(img_name)
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    
    # Setting the points for cropped image
    offset = 50
    left = offset
    top = offset
    right = width-offset
    bottom = height-offset*2
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    # im1.show()
    time.sleep(2)
    im1.save(img_name,"PNG")

    # create action chain object
    background = driver.find_element(by=By.XPATH, value="//canvas[@class='MyME0d widget-scene-canvas']")
    background.click()
    time.sleep(1)

    background.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    background.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)


if __name__ == '__main__':
    # set up the Selenium driver
    driver = webdriver.Chrome()

    # navigate to the Google Maps website
    driver.get("https://www.google.com/maps")

    # wait for the page to load
    time.sleep(5)
    
    for x in COORDINATE_LIST:
        worker(driver, x)