
#--------------------------------------------------------------
#ЗАДАНИЕ №1 HOME ДОБАВЛЕНИЕ КОММЕНТАРИЯ
#--------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
#скрол 600
driver.execute_script("window.scrollBy(0,600);")

driver.find_element(By.ID, 'text-22-sub_row_1-0-2-0-0').click()

driver.find_element(By.CSS_SELECTOR, '.tabs.wc-tabs>li:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, '.stars .star-5').click()

reviews=driver.find_element(By.ID, 'comment')
reviews.send_keys('Nice Book')

name=driver.find_element(By.ID, 'author')
name.send_keys('Alehandro')

e_mail=driver.find_element(By.ID, 'email')
e_mail.send_keys('123@mail.ru')

Btn=driver.find_element(By.CSS_SELECTOR, '#submit.submit').click()

driver.close()


#--------------------------------------------------------------
#ЗАДАНИЕ №1 HOME ДОБАВЛЕНИЕ КОММЕНТАРИЯ
#--------------------------------------------------------------