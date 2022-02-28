from cProfile import run
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from loginPage import LoginPage
from inventoryPage import InventoryPage
from checkOut import CheckOut

 
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# sign in
testLogin = LoginPage(driver)
testLogin.navigate("https://www.saucedemo.com/")
time.sleep(3)
testLogin.enter_username("standard_user")
testLogin.enter_password("secret_sauce")
testLogin.click_login()
time.sleep(2)

# Check if login succeeded
currentURL = driver.current_url
assert currentURL == "https://www.saucedemo.com/inventory.html"

time.sleep(1)

###### test inventory Page ######

#sort and check if sorting done correct
invPage = InventoryPage(driver)
invPage.changeSorting("product_sort_container","lohi")
driver.implicitly_wait(10)
invPage.check_low_to_high_sort()
time.sleep(3)

invPage.changeSorting("product_sort_container","hilo")
driver.implicitly_wait(10)
invPage.check_high_to_low_sort()
time.sleep(3)

invPage.changeSorting("product_sort_container","az")
driver.implicitly_wait(10)
invPage.check_A_to_Z_sort()
time.sleep(3)

invPage.changeSorting("product_sort_container","za")
driver.implicitly_wait(10)
invPage.check_Z_to_A_sort()
time.sleep(3)

invPage.click_item_page_and_verify("item_4_title_link")
time.sleep(3)

invPage.click_item_to_cart_and_verify('add-to-cart-sauce-labs-backpack')
time.sleep(3)

#CheckOut procedure
checkOutPage = CheckOut(driver)
checkOutPage.enter_firstname("Abanoub")
checkOutPage.enter_lastname("Waheed")
checkOutPage.enter_postal_code("11571")
time.sleep(2)
checkOutPage.click_continue()
time.sleep(2)
checkOutPage.click_finish()
time.sleep(2)

driver.quit()

#select = Select(driver.find_element_by_class_name('product_sort_container'))

# select by visible text
#select.select_by_visible_text('Banana')
#select.select_by_value('lohi')
#//*[@id="add-to-cart-sauce-labs-backpack"]
#//*[@id="add-to-cart-sauce-labs-bike-light"]
#https://www.saucedemo.com/checkout-step-two.html
#id="finish"