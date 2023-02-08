from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("\drivers")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

#go to url
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#get href
driver.find_element(By.XPATH, "//a[@class='blinkingText'][@href='https://rahulshettyacademy.com/documents-request']").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

email_text = driver.find_element(By.XPATH, "//p[@class='im-para red']//a").text
temp_text = email_text.split("@")[1]
username_text = temp_text.split(".")[0]
driver.close()

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(username_text)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()

assert "Shop Name" == driver.find_element(By.TAG_NAME, "h1").text


