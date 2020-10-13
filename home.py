#1. подключение webdriver
from selenium import webdriver 

#2. открытие ресурса
driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(20)
 
#3. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0,600);")

#4. review
book_name = driver.find_element_by_xpath("//h3[text()='Selenium Ruby']").click()
REVIEWS =  driver.find_element_by_css_selector("li.reviews_tab > a").click()
five_stars = driver.find_element_by_class_name("star-5").click()
your_review = driver.find_element_by_id("comment").send_keys("Nice book!") 
author_review_name = driver.find_element_by_id("author").send_keys("Zoya") 
author_review_email = driver.find_element_by_id("email").send_keys("Zoya@km.ru") 
submit_button = driver.find_element_by_id("submit").click()

driver.quit()
