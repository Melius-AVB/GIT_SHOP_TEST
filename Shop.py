from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
waits=WebDriverWait(driver, 5)
#                   -=Shop 10 =-
driver.find_element(By.ID, 'menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click()
time.sleep(1)
driver.find_element(By.ID, "wpmenucartli").click()
Bye = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a'))).click()

Fill_FN = waits.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
Fill_FN.send_keys("Aleksand")

Fill_2 = driver.find_element(By.ID, "billing_last_name")
Fill_2.send_keys("Bykovskiy")

Fill_3 = driver.find_element(By.ID, "billing_email")
Fill_3.send_keys("Melius87@mail.ru")

Fill_4 = driver.find_element(By.ID, "billing_phone")
Fill_4.send_keys("9876543211")

Fill_5 = driver.find_element(By.ID, "billing_email").clear()
driver.find_element(By.ID, "billing_email").send_keys("Melius87@mail.ru")

Country = driver.find_element(By.ID, "s2id_billing_country").click()
Country_chk = driver.find_element(By.ID, "s2id_autogen1_search")
Country_chk.send_keys("russia")
driver.find_element(By.ID, "select2-results-1").click()

Fill_6 = driver.find_element(By.ID, "billing_address_1")
Fill_6.send_keys("Novokolomiajskiy pr.")

Fill_7 = driver.find_element(By.ID, "billing_city")
Fill_7.send_keys("Saint-Peterburg")

Fill_8 = driver.find_element(By.ID, "billing_state")
Fill_8.send_keys("Saint-Peterburg")

Fill_9 = driver.find_element(By.ID, "billing_postcode")
Fill_9.send_keys("197375")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

driver.find_element(By.ID, "payment_method_cheque").click()
time.sleep(3)
driver.find_element(By.ID, "place_order").click()
time.sleep(1)
Check_1 = waits.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
Check_2 = waits.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tfoot>tr:nth-child(3)>td'), "Check Payments"))
driver.close()

#                  -=Shop 9-e=-
# driver.find_element(By.ID, 'menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="180"]').click()
# driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[data-product_id='182']").click()
# driver.find_element(By.LINK_TEXT, "Undo?").click()
# QTT = driver.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td:nth-child(5) input").clear()
# QTT = driver.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td:nth-child(5) input")
# QTT.send_keys("3")
# time.sleep(2)
# driver.find_element(By.NAME, "update_cart").click()
# time.sleep(2)
# Value = driver.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td:nth-child(5) input")
# V_check = Value.get_attribute("Value")
# assert V_check == "3"
# time.sleep(2)
# driver.find_element(By.NAME, "apply_coupon").click()
# time.sleep(2)
# chk = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error>li")
# chk_text = chk.text
# assert chk_text == "Please enter a coupon code."


#                  -=Shop 8-e =-

# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click()
# cart = driver.find_element(By.CSS_SELECTOR, "span.cartcontents")
# cart_text = cart.text
# print(cart_text)
# assert cart_text == "1 Item"
#
# cart_2 = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .amount")
# cart_text_2 = cart_2.text
# assert cart_text_2 == "₹180.00"
#
# driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
#
# SubTotal = waits.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal span.amount'), "₹180.00"))
# Total = waits.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'strong>span'), "₹183.60"))



#                   -=LogIn=-
# driver.find_element(By.ID, 'menu-item-50').click()
# Email=driver.find_element(By.ID, 'username')
# Email.send_keys('Melius87@mail.ru')
# time.sleep(1)
# password=driver.find_element(By.ID, 'password')
# password.send_keys('Ipconfig9190')
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, ('.login input:nth-child(3)')).click()
# time.sleep(1)
# driver.find_element(By.ID, 'menu-item-40').click()



#                   -=Shop 7-e img and price=-
# driver.find_element(By.CSS_SELECTOR, "img[title='Android Quick Start Guide']").click()
#
# price_1=driver.find_element(By.CSS_SELECTOR, ".price>del>span")
# Price_1_text=price_1.text
# assert Price_1_text == "₹600.00"
#
# price_2=driver.find_element(By.CSS_SELECTOR, ".price>ins>span")
# Price_2_text=price_2.text
# assert Price_2_text == "₹450.00"
#
# img=waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'wp-post-image'))).click()
# img_closed=waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close'))).click()




#                   -=Shop 6-e sort=-
# default=waits.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, 'select.orderby'), "menu_order"))
#
# sort_by = driver.find_element(By.CSS_SELECTOR, 'select.orderby')
# select = Select(sort_by)
# select.select_by_visible_text("Sort by price: high to low")
# default_2=waits.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, 'select.orderby'), "price-desc"))


#                   -=поиск 3-х товаров=-
# driver.find_element(By.LINK_TEXT, 'HTML').click()
# HTML_summ=driver.find_elements(By.CSS_SELECTOR, '.product.taxable')
# if len(HTML_summ) == 3:
#     print("ЗБС")
# else:
#     print("Чё за шляпа?")

#                 -=Поиск заголовка книги HTML=-
# driver.find_element(By.CSS_SELECTOR, '#content ul>li:nth-child(3)').click()
#
# text=driver.find_element(By.CSS_SELECTOR, '.product_title.entry-title')
# get_text=text.text
# print(get_text)
# assert get_text == "HTML5 Forms"

#driver.close()
