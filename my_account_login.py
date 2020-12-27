#1. подключение webdriver
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select  
import time 

#тестирую api
import requests
import urllib3


#2. открытие ресурса
driver = webdriver.Chrome() 
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 20) 

#3. вспомогательные функции

def login():# login
    driver.get("http://practice.automationtesting.in")
    my_account = driver.find_element_by_id("menu-item-50").click()
    user_login_email = driver.find_element_by_id("username").send_keys("zoya@km.ru")
    user_login_password = driver.find_element_by_id("password").send_keys("emailzoyakmru")
    login_button = driver.find_element_by_name("login").click()
    Shop = driver.find_element_by_id("menu-item-40").click()

def logout(): #logout
    my_account = driver.find_element_by_id("menu-item-50").click()
    logout = driver.find_element_by_xpath("//a[text()='Logout']").click()

def basket_container(): # содержимое корзины
    basket = driver.find_element_by_id("wpmenucartli") 
    time.sleep(10)
    count_item = driver.find_element_by_css_selector("span.cartcontents")
    count_amount = driver.find_element_by_css_selector("span.amount")
   
    count_item_text = count_item.text
    count_amount_text = count_amount.text

    print("В корзине", count_item_text)
    
    return count_item_text, basket 

def basket_container_clean(): #очистка корзины 
    
    count_item_text, basket = basket_container()
    
    if count_item_text != "0 Items":
        print("Необходимо очистить корзину")
        basket.click()
        time.sleep(10)
        count_item_text = driver.find_element_by_css_selector("span.cartcontents").text
        
        while count_item_text != "0 Items":
            try:
                driver.find_element_by_css_selector("td.product-remove > a").click() # удаляем item с помощью метода click
                count_item_text = basket_container() # снова проверяем значение items в корзине
            except:
                time.sleep(10)
                count_item = driver.find_element_by_css_selector("span.cartcontents")
                count_item_text = count_item.text
                break
               
    Shop = driver.find_element_by_id("menu-item-40").click()