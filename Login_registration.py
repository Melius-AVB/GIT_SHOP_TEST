from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.find_element(By.ID, 'menu-item-50').click()

#--------------------------------------------------------------
#ЗАДАНИЕ №2 Registration
#--------------------------------------------------------------
#
# Email=driver.find_element(By.ID, 'reg_email')
# Email.send_keys('Melius87@mail.ru')
# time.sleep(2)
# password=driver.find_element(By.ID, 'reg_password')
# password.send_keys('Ipconfig9190')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ('.register p:nth-child(4) .button')).click()
#
# time.sleep(8)
# driver.close()

#--------------------------------------------------------------
#ЗАДАНИЕ №3 Registration login
#--------------------------------------------------------------

driver.find_element(By.ID, 'menu-item-50').click()

Email=driver.find_element(By.ID, 'username')
Email.send_keys('Melius87@mail.ru')
time.sleep(2)
password=driver.find_element(By.ID, 'password')
password.send_keys('Ipconfig9190')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ('.login input:nth-child(3)')).click()
time.sleep(10)
Logout=driver.find_element(By.LINK_TEXT, 'Logout')
Logout_text=Logout.text
assert Logout_text == "Logout"
time.sleep(2)
driver.close()

