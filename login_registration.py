#1. подключение webdriver
from selenium import webdriver

#2. открытие ресурса
driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(20)

#3.регистрация аккаунта
#user email :zoya@km.ru
#user password:emailzoyakmru

my_account = driver.find_element_by_id("menu-item-50").click()
user_reg_email = driver.find_element_by_id("reg_email").send_keys("zoya@km.ru")
user_reg_password = driver.find_element_by_id("reg_password").send_keys("emailzoyakmru")
register_button = driver.find_element_by_name("register").click()

#4. логин в систему
driver.get("http://practice.automationtesting.in")
my_account = driver.find_element_by_id("menu-item-50").click()
user_login_email = driver.find_element_by_id("username").send_keys("zoya@km.ru")
user_login_password = driver.find_element_by_id("password").send_keys("emailzoyakmru")
login_button = driver.find_element_by_name("login").click()
logout = driver.find_element_by_xpath("//a[text()='Logout']")
if logout is not None:
    print("Logout is on page")

driver.quit()
