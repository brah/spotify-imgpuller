from selenium import webdriver
import requests
import time

# todo:
# Automatically reverse image on TinEye -> paid API i.e. has to be hacky implementation, Google(?)
driver = webdriver.Chrome()
user = input("Paste Spotify profile link:")
driver.get(user)
time.sleep(1)
src = driver.find_element_by_xpath(
    "/html/body/div[3]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[1]/div[1]/div[4]/img").get_attribute("src")
r = requests.get(src, allow_redirects=True)
open('profile_pic.jpg', 'wb').write(r.content)
driver.close
