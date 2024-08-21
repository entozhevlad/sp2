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

# Откроем страницу с формой контактов
driver.get("http://localhost:8000/contacts/")

# Найдем поля формы и кнопки
name_field = driver.find_element(By.NAME, "name")
email_field = driver.find_element(By.NAME, "email")
phone_field = driver.find_element(By.NAME, "phone")
message_field = driver.find_element(By.NAME, "message")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Заполним форму
name_field.send_keys("Тестовый Пользователь")
email_field.send_keys("test@example.com")
phone_field.send_keys("+79130000000")
message_field.send_keys("Это тестовое сообщение.")

# Отправим форму
submit_button.click()

# Подождем немного, чтобы увидеть результат
time.sleep(5)

# Проверим, что мы на главной странице
assert driver.current_url == "http://localhost:8000/"  # Замените на реальный URL вашей главной страницы

# Проверим наличие сообщения об успехе на главной странице
success_message = driver.find_element(By.TAG_NAME, "body").text

# Закроем браузер
driver.quit()
