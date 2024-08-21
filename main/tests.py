from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from .models import Service, Category
class ServiceViewSeleniumTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_service_view(self):
        # Создаем тестовые данные в базе данных
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')
        Service.objects.create(name='Service 1', price=100, category=category1, is_visible=True)
        Service.objects.create(name='Service 2', price=200, category=category2, is_visible=True)

        # Открываем страницу в браузере Selenium
        self.selenium.get(self.live_server_url + '/price')

        # Проверяем, что все категории и услуги отображаются на странице
        category1_element = self.selenium.find_element(By.XPATH, "//strong[contains(text(), 'Category 2')]")
        category2_element = self.selenium.find_element(By.XPATH, "//strong[contains(text(), 'Category 2')]")
        service1_element = self.selenium.find_element(By.XPATH, "//td[contains(text(), 'Service 1')]")
        service2_element = self.selenium.find_element(By.XPATH, "//td[contains(text(), 'Service 2')]")

        self.assertIsNotNone(category1_element)
        self.assertIsNotNone(category2_element)
        self.assertIsNotNone(service1_element)
        self.assertIsNotNone(service2_element)
