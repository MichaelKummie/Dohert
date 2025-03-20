import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Define Variable
pause = 5
url = "https://automationplayground.com/crm/login.html"


#visit url
driver.get(url)
time.sleep(pause)

#Valid email address login
Enter_email = driver.find_element(By.ID, "email-id")
Enter_email.send_keys("michaelkumekor@gmail.com")
time.sleep(pause)

#enter password
driver.find_element(By.ID, "password").send_keys("Kumekor1@")
time.sleep(pause)

#click on "remember me"
driver.find_element(By.ID, "remember").send_keys()
time.sleep(pause)

#click on submit button
driver.find_element(By.ID, "submit-id").click()
time.sleep(pause)

#click on "new customers"
driver.find_element(By.ID, "new-customer").click()
time.sleep(pause)

#input new customer email address
driver.find_element(By.ID, "EmailAddress").send_keys("deborahdoherty@gmail.com")
time.sleep(pause)

#input first name of customer
driver.find_element(By.ID, "FirstName").send_keys("deborah")
time.sleep(pause)

#input last name of customer
driver.find_element(By.ID, "LastName").send_keys("doherty")
time.sleep(pause)

#input city
driver.find_element(By.ID, "City").send_keys("Lagos")
time.sleep(pause)

#input state
driver.find_element(By.ID, "StateOrRegion").send_keys("Vermont")
time.sleep(pause)

#select gender
driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='female']").click()
time.sleep(pause)

#check the "add to promotional list button"
driver.find_element(By.CSS_SELECTOR, "input[name='promos-name'][value='promos-yes']").click()
time.sleep(pause)

#click on submit
driver.find_element(By.XPATH, "//button[@type='submit' and text()='Submit']").click()
time.sleep(pause)

#click on sign out
driver.find_element(By.CLASS_NAME, "nav-link").click()# Click 'Submit' button
time.sleep(pause)

