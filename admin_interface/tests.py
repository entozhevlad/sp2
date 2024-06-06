from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import environ
env = environ.Env()

# Укажите путь к вашему ChromeDriver
service = Service(executable_path='D:\\Soft\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Указываем URL сайта и данные для авторизации
base_url = "http://localhost:8000"
login_url = f"{base_url}/login/"
username = env("TEST_USERNAME")
password = env("TEST_PASSWORD")

def login(driver, username, password):
    driver.get(login_url)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

# Пример использования функции для тестирования авторизации
try:
    login(driver, username, password)
    time.sleep(2)  # Подождем, пока пройдет авторизация

    # Проверяем, что мы находимся на главной странице после авторизации


    # Здесь добавьте код для проверки других функций авторизации или выполнения других действий после входа в систему

finally:
    driver.quit()
