

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


#4.Shop: отображение страницы товара. shop >HTML5 Forms
print("#4.Shop: отображение страницы товара. shop >HTML5 Forms")
login()
#basket_container_clean()
book_HTML_V = driver.find_element_by_xpath("//h3[text()='HTML5 Forms']").click()
header_book = driver.find_element_by_css_selector(".product_title.entry-title")
header_book_get_text = header_book.text
assert header_book_get_text == "HTML5 Forms"

if header_book_get_text == "HTML5 Forms":
    print('Заголовок книги : HTML5 Forms')
else:
    print("ops")
logout()

#5. Shop: количество товаров в категории
print("#5. Shop: количество товаров в категории")
login()
basket_container_clean()
category_HTML = driver.find_element_by_css_selector("li.cat-item.cat-item-19 > a").click()
category_HTML_list = driver.find_elements(By.CLASS_NAME, "has-post-author")

if len(category_HTML_list) == 3:
    print("В категории HTML три книги")
else:
    print("ops")
logout()

#6. Shop: сортировка товаров
print("#6. Shop: сортировка товаров")
login()
#basket_container_clean()
def choice():
    if sort =="price-desc":
        print("Выбран вариант сортировки от большего к меньшему")
    else:
        print("Выбрана сортировка по-умолчанию")

Selector = driver.find_element_by_name("orderby")
sort = Selector.get_attribute("value")
choice()
sort_choise = Select(Selector)
sort_choise.select_by_value("price-desc")
Selector = driver.find_element_by_name("orderby")
sort = Selector.get_attribute("value")
choice()
logout()

#7. Shop: отображение, скидка товара
print("#7. Shop: отображение, скидка товара") 
login()
basket_container_clean()
book_Android_Quick_Start_Guide = driver.find_element_by_xpath("//h3[text()='Android Quick Start Guide']").click()
previous_price = driver.find_element_by_css_selector("div:nth-child(2) > p > del > span")
previous_price_get_text = previous_price.text

assert previous_price_get_text == "₹600.00"
if previous_price_get_text == "₹600.00":
    print('содержимое старой цены = "₹600.00"')
else:
    print("ops")

now_price = driver.find_element_by_css_selector("div:nth-child(2) > p > ins > span")
now_price_get_text = now_price.text

assert now_price_get_text == "₹450.00"
if now_price_get_text == "₹450.00":
    print('содержимое старой цены = "₹450.00"')
else:
    print("ops")

#8. Добавьте явное ожидание и нажмите на обложку книги
print("#8. Добавьте явное ожидание и нажмите на обложку книги")
img_cover = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".wp-post-image")))
cover_book = driver.find_element_by_class_name("wp-post-image").click()
 
cower_book_wait = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
            (By.ID, "fullResImage")))
close_button_wait = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".pp_details > a")))
close_click = driver.find_element_by_css_selector(".pp_details > a").click()

logout()

#9. Shop: проверка цены в корзине
print("#9. Shop: проверка цены в корзине")
login()

basket_container_clean()#очистка корзины
time.sleep(20)
book_HTML5_WebApp_Development = driver.find_element_by_xpath("//h3[text()='HTML5 WebApp Develpment']").click()
add_book = driver.find_element_by_css_selector("div.summary.entry-summary > form > button").click()
time.sleep(20)
basket = driver.find_element_by_id("wpmenucartli")
count_item = driver.find_element_by_css_selector("span.cartcontents")
count_amount = driver.find_element_by_css_selector("span.amount")
count_item_text = count_item.text
count_amount_text = count_amount.text


assert count_item_text == "1 Item"
assert count_amount_text == "₹180.00"

basket = driver.find_element_by_id("wpmenucartli").click() #обновляем поиск корзины

subtotal_price_wait= WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "tr.cart-subtotal > td > span")))
total_price_wait= WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.order-total > td >strong> span")))


logout()

#10. Shop: работа в корзине
print("#10. Shop: работа в корзине")
login()
basket_container_clean()#очистка корзины

driver.execute_script("window.scrollBy(0,300);")

add_book_HTML5_WebApp_Development = driver.find_element_by_css_selector('li.post-182>:nth-child(2)').click()
add_book_JS_Data_Structures_and_Algorithm= driver.find_element_by_css_selector('li.post-180>:nth-child(2)').click()
time.sleep(20)
basket = driver.find_element_by_id("wpmenucartli").click()
time.sleep(20)
del_first_item = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td.product-remove > a").click()

driver.find_element_by_xpath("//a[text()='Undo?']").click()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").clear()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").send_keys(3)

time.sleep(40)
UPDATE_BASKET_wait =  WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.NAME, "update_cart")))

print("UPDATE_BASKET")
UPDATE_BASKET = driver.find_element_by_name("update_cart").click()

quantity_updated = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
Value_quantity_updated = quantity_updated.get_attribute("value")

assert Value_quantity_updated == "3"
print('value элемента quantity для "JS Data Structures and Algorithm" равно 3')
time.sleep(20)
APPLY_COUPON = driver.find_element_by_name("apply_coupon").click()

warning = driver.find_element_by_css_selector("div.woocommerce > ul > li")
warning_text = warning.text
assert "Please enter a coupon code" in warning_text 

print('возникло сообщение: "Please enter a coupon code."')

logout()

#11. Shop: покупка товара
print('#11. Shop: покупка товара')
driver.get("http://practice.automationtesting.in")
Shop = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0,300);")
add_book_HTML5_WebApp_Development = driver.find_element_by_css_selector('li.post-182>:nth-child(2)').click()
basket_wait = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID,"wpmenucartli")))
basket = driver.find_element_by_id("wpmenucartli").click()

checkout_wait = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CLASS_NAME,"wc-forward")))
checkout = driver.find_element_by_class_name("wc-forward").click()


# данные пользователя
#First_Name: Сергей
#Last_Name: Вавилов
#Email: serV@kmm.ru
#Phone:  1210459699
#Gender: Male
#Country: Russia
#street: Первая
#city: Омск
#satate: Омская
#postindex: 254789
#Year: 1990 
#Month:February 
#Day: 10
#Password: p111111P
first_name_wait = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
first_name = driver.find_element_by_id("billing_first_name").send_keys("Сергей")
last_name = driver.find_element_by_id("billing_last_name").send_keys("Вавилов")
email = driver.find_element_by_id("billing_email").send_keys("serV@kmm.ru")
phone = driver.find_element_by_id("billing_phone").send_keys("1210459699")
country_selector = driver.find_element_by_id("s2id_billing_country").click()
countru_search = driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
country_Russia = driver.find_element_by_id("select2-result-label-393").click()
street = driver.find_element_by_id("billing_address_1").send_keys("Первая")
city = driver.find_element_by_id("billing_city").send_keys("Омск")
state = driver.find_element_by_id("billing_state").send_keys("Омская")
postcode = driver.find_element_by_id("billing_postcode").send_keys("254789")

driver.execute_script("window.scrollBy(0,600);")
time.sleep(10)
payment_method_cheque = driver.find_element_by_id("payment_method_cheque").click()

place_order = driver.find_element_by_id("place_order").click()

thanks = driver.find_element_by_class_name("woocommerce-thankyou-order-received")
Thanks_wait = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
Check_Payments_wait = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR," li.method > strong"),"Check Payments"))

# отсюда работаю с git
print("# отсюда работаю с git")
#12 branch shop7-home-page-with-three-sliders-only  

print("#12. the Home page has Three Sliders ")
login()
basket_container_clean()#очистка корзины

home = driver.find_element_by_xpath("//a[text()='Home']").click()
three_sliders = driver.find_elements(By.CLASS_NAME,"n2-ss-slide-background-image.n2-ss-slide-fill.n2-ow")

if len(three_sliders) == 3:
    print("the Home page has Three Sliders")
else:
    print("ops")
#print("yes")
logout()

#13 branch shop8 2.Home page with three Arrivals only  
print("#13. Home page with three Arrivals only ")
login()
basket_container_clean()#очистка корзины

home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

logout()


#14 branch shop9 3.Home page - Images in Arrivals should navigate 
print("#14. Images in Arrivals should navigate ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")

logout()


#15 branch shop10 4. Home page - Arrivals-Images-Description  
print("#15. Home page - Arrivals-Images-Description")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")

description = driver.find_element_by_css_selector("li.description_tab>a").click()
description_text= driver.find_element_by_id("tab-description")
assert description_text
print("There should be a description regarding that book the user clicked on")
logout()

#16 branch shop11  Home page - Arrivals-Images-Reviews
print("#16.  Home page - Arrivals-Images-Reviews")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
reviews_tab = driver.find_element_by_class_name("reviews_tab").click()
reviews = driver.find_element_by_class_name("woocommerce-Reviews-title")
assert reviews != None
print("There is a Reviews here")
logout()

#17 branch shop12 Home page - Arrivals-Images-Add to Basket             
print("#17.Home page - Arrivals-Images-Add to Basket  ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item = driver.find_element_by_css_selector("span.cartcontents")
count_item_text = count_item.text
assert count_item_text != "0 items"
print("Your item was added")
logout()

#пример тестирования запроса API
print("#пример тестирования запроса API")

http = urllib3.PoolManager()
r = http.request('GET', 'http://practice.automationtesting.in/product/html5-forms/')
print("Дата запроса:" , r.headers['Date'])
print("Код ответа:", r.status)

#18 branch shop13 Home page - Arrivals-Add to Basket with more books   
print("#18.Home page - Arrivals-Add to Basket with more books  ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"

in_stock = driver.find_element_by_class_name("in-stock").text
#print(in_stock) #сообщение о максимальном количестве книг для заказа 
in_stock_split = in_stock.split(" ")
in_stock_count = int(in_stock_split[0])+1
print("Значение превышающее допустимое",in_stock_count)

counter_add_book = driver.find_element_by_class_name("input-text.qty.text")
counter_add_book.clear()
counter_add_book_chenge = driver.find_element_by_class_name("input-text.qty.text").send_keys(in_stock_count)

validationMessage = counter_add_book.get_attribute("validationMessage");
assert validationMessage == "Значение должно быть меньше или равно 494."


print("Предупреждение",validationMessage)
logout()

#19 branch shop14 Home-Arrivals-Add to Basket-Items-Coupon             
print("#19. Home-Arrivals-Add to Basket-Items-Coupon   ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Selenium Ruby']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"
print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()
coupon_input = driver.find_element_by_id("coupon_code").send_keys('krishnasakinala')

coupon_apply = driver.find_element_by_name("apply_coupon").click()

coupon_admit = driver.find_element_by_class_name("coupon-krishnasakinala")
coupon_admit_text = coupon_admit.find_element_by_xpath("//td[@data-title='Coupon: krishnasakinala']").text
print("Применена скидка", coupon_admit_text)
assert coupon_admit_text == "-₹50.00, Free shipping coupon [Remove]"
logout()

 
#20 branch shop15  Home-Arrivals-Add to Basket-Items-Coupon value<450                  
print("#20. Home-Arrivals-Add to Basket-Items-Coupon value<450 : добавть книгу, стоимость которой меньше 450р.  ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")

each_arrivel = driver. find_element_by_xpath("//img[@alt='Mastering JavaScript']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"

print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()
coupon_input = driver.find_element_by_id("coupon_code").send_keys('krishnasakinala')

coupon_apply = driver.find_element_by_name("apply_coupon").click()
message_coupon = driver.find_element_by_class_name("woocommerce-error")
print(message_coupon.text)
assert message_coupon.text == "The minimum spend for this coupon is ₹450.00."
logout()


#21 branch shop16   Home-Arrivals-Add to Basket-Items-Remove book            
print("#21 Home-Arrivals-Add to Basket-Items-Remove book  ")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")
each_arrivel = driver. find_element_by_xpath("//img[@alt='Mastering JavaScript']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"

print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()                                         
driver.find_element_by_css_selector("td.product-remove > a").click() # удаляем item с помощью метода click
remote = driver.find_element_by_class_name("woocommerce-message").text
assert remote == "Mastering JavaScript removed. Undo?"
logout()

#22 branch shop17   Home-Arrivals-Add to Basket-Items-Add book 
print("#22  Home-Arrivals-Add to Basket-Items-Add book")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")
each_arrivel = driver. find_element_by_xpath("//img[@alt='Mastering JavaScript']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"

print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").clear()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").send_keys(3)

#time.sleep(40)
UPDATE_BASKET_wait =  WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.NAME, "update_cart")))


UPDATE_BASKET = driver.find_element_by_name("update_cart").click()
update_message = driver.find_element_by_class_name("woocommerce-message").text
assert update_message == "Basket updated."
print("Basket updated.")
logout()



#23 branch shop18    Home-Arrivals-Add to Basket-Items-Check-out-Book Final price      
print("#23 Home-Arrivals-Add to Basket-Items-Check-out-Book Final price")
login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")
each_arrivel = driver. find_element_by_xpath("//img[@alt='Mastering JavaScript']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"

print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()

count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()


subtotal_row = driver.find_element_by_class_name("cart-subtotal")
subtotal = subtotal_row .find_element_by_class_name("woocommerce-Price-amount.amount").text

Tax_row = driver.find_element_by_class_name("tax-rate.tax-rate-roaming-tax-1")
Tax = Tax_row.find_element_by_class_name("woocommerce-Price-amount.amount").text

Total_row = driver.find_element_by_class_name("order-total")
Total = Total_row.find_element_by_class_name("woocommerce-Price-amount.amount").text

import re
pattern = r"₹"
subtotal_float = float(re.sub(pattern,"",subtotal))
Tax_float = float(re.sub(pattern,"",Tax))
Total_float = float(re.sub(pattern,"",Total))

assert Total_float == Tax_float + subtotal_float, t_summ
print("Общая сумма подсчитана верно")
logout()


#24 branch shop19   Home-Arrivals-Add to Basket-Items-Check-out functionality  '''               
print("#24 Home-Arrivals-Add to Basket-Items-Check-out functionality ")
#login()
basket_container_clean()#очистка корзины
home = driver.find_element_by_xpath("//a[text()='Home']").click()
new_arrivals = driver.find_elements(By.CLASS_NAME, "products")
if len(new_arrivals) == 3:
    print("the Home page has Three Arrivals")
else:
    print("ops")
each_arrivel = driver. find_element_by_xpath("//img[@alt='Mastering JavaScript']").click()
add_button_is_here = driver.find_element_by_class_name("single_add_to_cart_button")
add_button_is_here_wait = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"single_add_to_cart_button")))
assert add_button_is_here!= None, "'Add book' is not clickable"

print("The image in the Arrivals is navigating to next page where the user can add that book into his basket")
Add_to_basket = driver.find_element_by_class_name("single_add_to_cart_button.button.alt").click()
count_item_text = basket_container()
assert count_item_text != "0 Items"
basket = driver.find_element_by_id("wpmenucartli").click()
subtotal_row = driver.find_element_by_class_name("cart-subtotal")
subtotal = subtotal_row .find_element_by_class_name("woocommerce-Price-amount.amount").text

Tax_row = driver.find_element_by_class_name("tax-rate.tax-rate-roaming-tax-1")
Tax = Tax_row.find_element_by_class_name("woocommerce-Price-amount.amount").text

Total_row = driver.find_element_by_class_name("order-total")
Total = Total_row.find_element_by_class_name("woocommerce-Price-amount.amount").text

import re
pattern = r"₹"
subtotal_float = float(re.sub(pattern,"",subtotal))
Tax_float = float(re.sub(pattern,"",Tax))
Total_float = float(re.sub(pattern,"",Total))

assert (Total_float - Tax_float - subtotal_float) < 1 , t_summ
print("Общая сумма подсчитана верно")


ProceedtoCheckout = driver.find_element_by_class_name("wc-forward").click()
current_page = driver.current_url
assert current_page == "http://practice.automationtesting.in/checkout/"
print(current_page)

#logout()

#25 branch shop20   Home-Arrivals-Add to Basket-Items-Check-out-Payment Gateway                   
print("#25 Home-Arrivals-Add to Basket-Items-Check-out-Payment Gateway Проверка выводит результат для  PayPal Express Checkout")
#Now user can fill his details in billing details form 
#and can opt any payment in the payment gateway like
# Direct bank transfer,cheque,cash or paypal.


# модуль обработки исключений  наличия элемента на странице
Billing_Details_by_xpath = "//h3[text()='Billing Details']"
from selenium.common.exceptions import NoSuchElementException  
    
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
check_exists_by_xpath(Billing_Details_by_xpath) # 
billing_info = {
"billing_first_name":"Томм",
"billing_last_name":"Reddle",
"billing_email":"Tomm@lm.com",
"billing_phone":"891196587",
"select2-input":"Russia",
"billing_address_1":"Street First",
"billing_city":"Town",
"billing_state":"State",
"billing_postcode":"125478",

}

billing_first_name = driver. find_element_by_id( "billing_first_name").send_keys("Томм")
billing_last_name = driver. find_element_by_id( "billing_last_name").send_keys("Reddle")
billing_email  = driver. find_element_by_id("billing_email").send_keys("Tomm@lm.com")
billing_phone  = driver. find_element_by_id("billing_phone").send_keys("891196587")
Country = driver. find_element_by_id("select2-chosen-1").click()
search_country = driver.find_element_by_class_name("select2-input").send_keys("Russia")
billing_address_1 = driver. find_element_by_id("billing_address_1").send_keys("Street First")
billing_city = driver. find_element_by_id("billing_city").send_keys("Town")
billing_state = driver. find_element_by_id("billing_state").send_keys("State")
billing_postcode  = driver. find_element_by_id("billing_postcode").send_keys("125478")

#driver.execute_script("return arguments[0].scrollIntoViwe(true);",payment_method_bacs)
driver.execute_script("window.scrollBy(0,400);")

driver.find_element_by_class_name("select2-drop-mask").click()

Check_Payments = driver.find_element_by_id("payment_method_cheque")
Check_Payments.click()

payment_method_cod = driver.find_element_by_id("payment_method_cod")
payment_method_cod.click()

payment_method_ppec_paypal = driver.find_element_by_id("payment_method_ppec_paypal")
payment_method_ppec_paypal.click()


payment_method_ppec_paypal_attr = payment_method_ppec_paypal.get_attribute("checked")
print(payment_method_ppec_paypal_attr)

assert payment_method_ppec_paypal_attr == "true"
payment_method_cod_attr = payment_method_cod.get_attribute("checked")

Check_Payments_attr = Check_Payments.get_attribute("checked")

choise_paypal = False
choise_cod= False
choise_Pay= False
if payment_method_ppec_paypal_attr == "true":
    choise_paypal = True
if payment_method_cod_attr == "true":
    choise_cod = True
if Check_Payments_attr == "true":
    choise_Pay = True

place_order = driver.find_element_by_id("place_order").click()

if choise_paypal == True:
    error = driver.find_element_by_class_name("woocommerce-error") .text
    assert "Payment error:" in error
    print("Этот метод оплаты требует дополнительных телодвижений")

# woocommerce-thankyou-order-received

print("Успешно")



#driver.quit()


