import string
import time
from selenium import webdriver

#set vars
sciezkaSelen = "C:/SeleniumDrivers/chromedriver.exe"
imie = "Hubert"
nazwisko = "Gorol"
biznes = "RPA"
mejl = "hubert@gorol.com"

# set driver
driver = webdriver.Chrome(sciezkaSelen)
driver.get("https://phptravels.com/demo/")

# Sleep for 1 seconds
time.sleep(1)

# get elements
firstName = driver.find_element_by_name("first_name")
lastName = driver.find_element_by_name("last_name")
businessName = driver.find_element_by_name("business_name")
emailAdress = driver.find_element_by_name("email")

num1 = driver.find_element_by_id("numb1").text
num2 = driver.find_element_by_id("numb2").text
# sum numbers
wynik = int(num1) + int(num2)

result = driver.find_element_by_id("number")
submitButton = driver.find_element_by_id("demo")

# instert vars
firstName.click()
firstName.send_keys(imie)
lastName.click()
lastName.send_keys(nazwisko)
businessName.click()
businessName.send_keys(biznes)
emailAdress.click()
emailAdress.send_keys(mejl)
result.click()
result.send_keys(wynik)

# Sleep for 1 seconds
time.sleep(1)

# click submit
submitButton.click()