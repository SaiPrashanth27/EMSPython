import time

import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://sem-demo.devsbot.com/app/signin")
driver.find_element(By.ID, "email").send_keys("saiprashanth.s@niraltek.com")
print("Entered the email")
driver.find_element(By.ID, "password").send_keys("Welcome@1to3")
print("Password is Entered")
driver.find_element(By.XPATH, "//*[text()='Login']").click()
print("login button click and login successfully")
time.sleep(20)
