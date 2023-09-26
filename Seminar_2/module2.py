'''Задание 1. Оптимизация примера из лекции
Доработать пример из лекции следующим образом:
вынести все локаторы элементов в фикстуры в conftest.py
вынести ожидаемый результат в фикстуру в conftest.py
добавить завершение работы Selenium после теста
вынести время ожидания в конфигурационный файл testdata.yam'''

import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata2.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)

        # браузер работает в фоном режиме, не открывается
        # options.add_argument('--headless')
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(testdata["sleep_time"])
        # открываем окно максимально развернутым на весь экран
        self.driver.maximize_window()
        # открываем адрес сайта
        self.driver.get(address)

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

'''
    def close(self):
        self.driver_close()
'''