import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/revantkantamneni/Desktop/Revant_Nike_Bot/chromedriver')

#Login
urs = 'revantkantamneni@gmail.com'
urs2 = 'tumbletipsforyou@gmail.com'
pw = '' #input password here
shoe_size = 'M 10.5 / W 12'

#Load Website and Click Sign In
driver.get('https://www.nike.com/launch/t/chuck-taylor-all-star-crater-white')
#https://www.nike.com/launch/t/air-force-1-low-triple-white')
#https://www.nike.com/launch/t/kyrie-6-asia-irving']
#https://www.nike.com/launch/t/killshot-og-midnight-navy
time.sleep(1.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Join / Log In')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='SIGN IN']")))

#Inputs Login Details
email_input = driver.find_element_by_xpath("//input[@name='emailAddress']") #email_input = driver.find_element_by_name('emailAddress')
email_input.clear()
email_input.send_keys(urs)
password = driver.find_element_by_xpath("//input[@name='password']") #password = driver.find_element_by_name('password')
password.clear()
password.send_keys(pw)
driver.find_element_by_xpath("//input[@value='SIGN IN']").click() #Note Needs to Be Run twice due to blocking

#Wait till drop time 
timeOfDrop = datetime.now().hour + 1
print(timeOfDrop)
while datetime.now().hour != timeOfDrop:
	time.sleep(0.1)

#Refresh Website, Click Size of Shoes
start = time.time()
driver.refresh()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='gen-nav-footer']/footer/div/div[2]/div[2]/ul/li[4]/a"))) #sizeSelect = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='size-grid-dropdown size-grid-button'][.='M 9.5 / W 11']"))) #USE contactination to incorporate variable
sizeSelect = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'M 10.5 / W 12.5')]"))) #USE contactination to incorporate variable
time.sleep(1.5)
sizeSelect.click()

#Add To Cart
cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'ADD TO CART')]")))
cart.click()

#Checkout
checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Checkout')]"))) #Goes straight to checkout
checkout.click()

#Scroll To Bottom of Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

print(time.time() - start)
time.sleep(1.5)

#driver.get_screenshot_as_file("bill.png") #Billing Screenshot




