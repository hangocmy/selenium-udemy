from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CssSelector, Class name, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Hello")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message) #Success! The Form has been submitted successfully!.
assert "Success" in message