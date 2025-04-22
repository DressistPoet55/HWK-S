from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.implicitly_wait(1)
browser.get("https://www.saucedemo.com/")

try:
    # Экран логина:
    log_name = browser.find_element(By.ID, "user-name")
    log_name.send_keys("standard_user")
    log_pass = browser.find_element(By.ID, "password")
    log_pass.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)

    # Экран главной страницы:
    text_products = browser.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
    if "Products" in text_products:
        print("На главной странице: Products")
    else:
        print("Не удалось перейти на главную страницу")
    prod_add = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    prod_add.click()
    shp_cart = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    shp_cart.click()
    time.sleep(1)

    # Корзина:
    text_cart = browser.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
    if "Your Cart" in text_cart:
        print("В корзине: Your Cart")
    else:
        print("Не удалось перейти в корзину")
    checkout_btn = browser.find_element(By.ID, "checkout")
    checkout_btn.click()
    check_name = browser.find_element(By.ID, "first-name")
    check_name.send_keys("First")
    check_sur = browser.find_element(By.NAME, "lastName")
    check_sur.send_keys("Last")
    check_postid = browser.find_element(By.ID, "postal-code")
    check_postid.send_keys("123456")
    chck_cont_btn = browser.find_element(By.ID, "continue")
    chck_cont_btn.click()
    time.sleep(1)
    finish_btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button")
    finish_btn.click()
    success_message = browser.find_element(By.CLASS_NAME, "complete-text").text
    if "Your order has been dispatched" in success_message:
        print("Текст успешного оформления заказа найден")
    else:
        print("Текст успешного оформления заказа отсутствует")

finally:
    browser.quit()
