import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class InventoryPage():
    def __init__(self,driver) :
        self.driver = driver
    
    def navigate(self, urlLogin):
        self.driver.get(urlLogin)

    def changeSorting(self, locatorClass, option):
        self.sel = Select (self.driver.find_element_by_class_name (locatorClass))
        self.sel.select_by_value (option)

    def check_A_to_Z_sort(self):
        items_names = self.driver.find_elements_by_class_name("inventory_item_name")
        for name in items_names:
            name_text=name.text
            print(name_text)
            names_list=[]
            names_list.append(name_text)
        sorted_names = sorted(names_list)   
        if(names_list == sorted_names):
            print("'A_to_Z' sorting working ")
        else: 
            print("'A_to_Z' sorting not working")
    
    def check_Z_to_A_sort(self):
        items_names = self.driver.find_elements_by_class_name("inventory_item_name")
        for name in items_names:
            name_text=name.text
            print(name_text)
            names_list=[]
            names_list.append(name_text)
        sorted_names = sorted(names_list)
        reversed_names = sorted_names.reverse()
        if(names_list == reversed_names):
            print("'Z_to_A' sorting working ")
        else: 
            print("'Z_to_A' sorting not working")

    def check_low_to_high_sort(self):
        items_prices = self.driver.find_elements_by_class_name ("inventory_item_price")
        for price in items_prices:
            price_text=price.text
            price_text = price_text.replace('$','')
            value = float(price_text)
            prices_values=[]
            prices_values.append(value)
        sorted_prices = sorted(prices_values)
        if(prices_values == sorted_prices):
            print("'low_to_high' sorting working ")
        else: 
            print("'low_to_high' sorting not working")
        
    def check_high_to_low_sort(self):
        items_prices = self.driver.find_elements_by_class_name ("inventory_item_price")
        for price in items_prices:
            price_text=price.text
            price_text = price_text.replace('$','')
            value = float(price_text)
            prices_values=[]
            prices_values.append(value)
        sorted_prices = sorted(prices_values)
        reversed_prices = sorted_prices.reverse()
        if(prices_values == reversed_prices):
            print("'high_to_low' sorting working ")
        else: 
            print("'high_to_low' sorting not working")
            
    def click_item_page_and_verify(self,item_full_id):
        self.driver.find_element_by_id(item_full_id).click()    
        item_id = item_full_id[5]
        currentURL = self.driver.current_url
        assert currentURL == "https://www.saucedemo.com/inventory-item.html?id=" + str(item_id)
        print("item page " + str(item_id)+" opened")
    

    def click_item_to_cart_and_verify(self,item_id):
        self.driver.find_element_by_id(item_id).click()    
        item_shopped = self.driver.find_element_by_class_name("shopping_cart_badge")
        assert int(item_shopped.text) == 1 
        self.driver.find_element_by_class_name("shopping_cart_badge").click()
        time.sleep(2)
        self.driver.find_element_by_id("checkout").click()
        time.sleep(2)
        currentURL = self.driver.current_url
        assert currentURL == "https://www.saucedemo.com/checkout-step-one.html"
        print("check out page opened")

