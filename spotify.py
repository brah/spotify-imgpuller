from selenium import webdriver
import requests
import time
from tineye import TinEye, TinEyePhoto
# todo:
# automatically reverse search the image (alexs 300iq idea)
driver = webdriver.Chrome()
user = input("paste spotify user link:")
driver.get(user)
time.sleep(1)
src = driver.find_element_by_xpath(
    "/html/body/div[3]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[1]/div[1]/div[4]/img").get_attribute("src")
r = requests.get(src, allow_redirects=True)
open('profile_pic.jpg', 'wb').write(r.content)
driver.close
