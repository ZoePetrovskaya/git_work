#1. подключение webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select  
import time 

#2. открытие ресурса
driver = webdriver.Chrome() 
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


def basket_container(): #очистка корзины
    basket = driver.find_element_by_id("wpmenucartli") 
    time.sleep(10)
    count_item = driver.find_element_by_css_selector("span.cartcontents")
    count_amount = driver.find_element_by_css_selector("span.amount")
   
    #count_item_text = count_item.text
    count_item_text = count_item.text
    count_amount_text = count_amount.text
    print("В корзине", count_item_text)
    #print(count_amount_text)
    #
    #print(count_item_text)
    #count_amount_text = count_amount.text
    #print(count_amount_text)
    if count_item_text != "0 items":
        basket.click()
        time.sleep(10)
        while count_item != "0 items":
            try:
                del_item = driver.find_element_by_css_selector("td.product-remove > a").click()
            except:
                time.sleep(10)
                count_item = driver.find_element_by_css_selector("span.cartcontents")
                count_item_text = count_item.text
                print("В корзине", count_item_text)
                break

    #assert count_item_text == "0 items"
    Shop = driver.find_element_by_id("menu-item-40").click()


#4.Shop: отображение страницы товара. shop >HTML5 Forms
print("#4.Shop: отображение страницы товара. shop >HTML5 Forms")
login()
#basket_container()
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
basket_container()
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
#basket_container()
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
basket_container()
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

basket_container()#очистка корзины
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
basket_container()#очистка корзины

driver.execute_script("window.scrollBy(0,300);")

add_book_HTML5_WebApp_Development = driver.find_element_by_css_selector('li.post-182>:nth-child(2)').click()
add_book_JS_Data_Structures_and_Algorithm= driver.find_element_by_css_selector('li.post-180>:nth-child(2)').click()
time.sleep(20)
basket = driver.find_element_by_id("wpmenucartli").click()

del_first_item = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td.product-remove > a").click()

driver.find_element_by_xpath("//a[text()='Undo?']").click()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").clear()
quantity = driver.find_element_by_css_selector("form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").send_keys(3)

#time.sleep(40)
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
basket_container()#очистка корзины

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
basket_container()#очистка корзины

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
basket_container()#очистка корзины
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


#print("yes")
driver.quit()


