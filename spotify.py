from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests

# todo:
# Automatically reverse image on TinEye -> paid API i.e. has to be hacky implementation, Google(?)

# Suppress weird Bluetooth adapter error/warning
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
# Running headless is slow for some reason, this will just hide the browser to not intefere
driver.set_window_position(-3000, 0)

try:
    userLink = input("Paste Spotify profile link: ")
finally:
    driver.get(userLink)

try:
    element = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(
        "/html/body/div[3]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[1]/div[1]/div[4]/img"))
finally:
    src = element.get_attribute("src")
    r = requests.get(src, allow_redirects=True)
    open('profile_img.jpg', 'wb').write(r.content)
driver.quit