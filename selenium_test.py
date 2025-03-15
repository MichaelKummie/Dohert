import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#visit the url
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

#Valid email address login
driver.find_element(By.ID, "email-id").send_keys("michaelkumekor@gmail.com")
time.sleep(5)

#enter password
driver.find_element(By.ID, "password").send_keys("Kumekor1@")
time.sleep(5)

#click on "remember me"
driver.find_element(By.ID, "remember").send_keys()
time.sleep(5)

#click on submit button
driver.find_element(By.ID, "submit-id").click()
time.sleep(5)

#click on "new customers"
driver.find_element(By.ID, "new customer").click()
time.sleep(5)

#input new customer email address
driver.find_element(By.ID, "EmailAddress").send_keys("deborahdoherty@gmail.com")
time.sleep(5)

#input first name of customer
driver.find_element(By.ID, "Firstname").send_keys("deborah")
time.sleep(5)

#input last name of customer
driver.find_element(By.ID, "Lastname").send_keys("doherty")
time.sleep(5)

#input city
driver.find_element(By.ID, "City").send_keys("Alimosho")
time.sleep(5)

#input state
driver.find_element(By.ID, "State").send_keys("Lagos")
time.sleep(5)

#select gender type
driver.find_element(By.XPATH,"//*[@id='loginform']div/div/div/div/form/div[6]/input[2]").click()
time.sleep(5)

#check the "add to promotional list button
driver.find_element(By.XPATH,"//*[@id='loginform']div/div/div/div/form/div[7]/input").click()
time.sleep(5)

#click on submit
driver.find_element(By.XPATH,"//*[@id='loginform']div/div/div/div/form/button").click()
time.sleep(5)

#click on sign
driver.find_element(By.XPATH,"/html/body/nav/u1/1i/a").click()
time.sleep(5)

time.sleep(5)
