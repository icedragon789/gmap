from selenium import webdriver
from selenium.webdriver.common.by import By

# import urllib.request
# import time

# # set up the Selenium driver
# driver = webdriver.Chrome()

# # navigate to the Google Maps website
# driver.get("https://www.google.com/maps")

# # wait for the page to load
# time.sleep(5)

# # search for the location you want to download a satellite image for
# search_box = driver.find_element(by=By.XPATH, value="//input[@id='searchboxinput']")
# search_box.send_keys("San Francisco")
# search_box.submit()




# switch to satellite view
# satellite_button = driver.find_element(by=By.XPATH, value="//button[@data-value='Satellite']")
# satellite_button.click()



# # zoom in to the desired level
# for i in range(10):
#     zoom_in_button = driver.find_element(by=By.XPATH, value="//button[@data-tooltip='Zoom in']")
#     zoom_in_button.click()

# get the URL of the current view
# current_url = driver.current_url

# # download the image
# urllib.request.urlretrieve(current_url, "satellite_image.png")

# # close the driver
# driver.quit()
