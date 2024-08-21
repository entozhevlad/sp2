from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


try:
    # Логин
    login(driver, username, password)
    time.sleep(2)  # Подождем, пока пройдет авторизация

    # Добавление категории
    driver.get(f"{base_url}/admin_sp/add_category/")
    category_name = "Тестовая категория"
    category_field = driver.find_element(By.NAME, "name")
    category_field.send_keys(category_name)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка добавления категории
    driver.get(f"{base_url}/admin_sp/")
    wait_for_element(driver, By.XPATH, f"//td[text()='{category_name}']")

    # Добавление услуги
    driver.get(f"{base_url}/admin_sp/add_service/")
    service_name = "Тестовая услуга"
    service_price = "1000"
    service_name_field = driver.find_element(By.NAME, "name")
    service_price_field = driver.find_element(By.NAME, "price")
    service_name_field.send_keys(service_name)
    service_price_field.send_keys(service_price)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка добавления услуги
    driver.get(f"{base_url}/admin_sp/")
    wait_for_element(driver, By.XPATH, f"//td[text()='{service_name}']")

    # Изменение услуги
    edit_service_link = driver.find_element(By.XPATH,
                                            f"//td[text()='{service_name}']/following-sibling::td/a[text()='Изменить']")
    edit_service_link.click()
    new_service_name = "Тестовая услуга измененная"
    service_name_field = driver.find_element(By.NAME, "name")
    service_name_field.clear()
    service_name_field.send_keys(new_service_name)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка изменения услуги
    driver.get(f"{base_url}/admin_sp/")
    wait_for_element(driver, By.XPATH, f"//td[text()='{new_service_name}']")

    # Изменение категории
    edit_category_link = driver.find_element(By.XPATH,
                                             f"//td[text()='{category_name}']/following-sibling::td/a[text()='Изменить']")
    edit_category_link.click()
    new_category_name = "Тестовая категория измененная"
    category_name_field = driver.find_element(By.NAME, "name")
    category_name_field.clear()
    category_name_field.send_keys(new_category_name)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка изменения категории
    driver.get(f"{base_url}/admin_sp/")
    wait_for_element(driver, By.XPATH, f"//td[text()='{new_category_name}']")

    # Удаление услуги
    delete_service_link = driver.find_element(By.XPATH,
                                              f"//td[text()='{new_service_name}']/following-sibling::td/a[text()='Удалить']")
    delete_service_link.click()
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка удаления услуги
    driver.get(f"{base_url}/admin_sp/")
    time.sleep(1)
    assert not driver.find_elements(By.XPATH, f"//td[text()='{new_service_name}']")

    # Удаление категории
    delete_category_link = driver.find_element(By.XPATH,
                                               f"//td[text()='{new_category_name}']/following-sibling::td/a[text()='Удалить']")
    delete_category_link.click()
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверка удаления категории
    driver.get(f"{base_url}/admin_sp/")
    time.sleep(1)
    assert not driver.find_elements(By.XPATH, f"//td[text()='{new_category_name}']")

finally:
    driver.quit()
