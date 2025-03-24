import allure
import requests
from selenium.webdriver.common.by import By

base_url = "https://web-gate.chitai-gorod.ru/"
access_token = ""


class ChitaiGorod:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Зайти на сайт")
    def go_to(self):
        """
            Эта функция открывает сайт
        """
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Задать название: {term}")
    def name_ui(self, term: str):
        """
            Эта функция очищает поле для ввода
            и задает название книги
        """
        with allure.step("Очистить поле ввода"):
            input = self.driver.find_element(By.CSS_SELECTOR, 'input.header-search__input')
            input.clear()
        with allure.step("Внести название в поле ввода"):
            input.send_keys(term)
        with allure.step("Нажать на кнопку поиска"):
            self.driver.find_element(By.CSS_SELECTOR,
                                 'button.header-search__button').click()
            

        
