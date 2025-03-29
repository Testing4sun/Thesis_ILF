import allure
from selenium.webdriver.common.by import By


class ChitaiGorodUI:

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
            input = self.driver.find_element(By.CSS_SELECTOR,
                                             'input.header-search__input')
            input.clear()
        with allure.step("Внести название в поле ввода"):
            input.send_keys(term)
        with allure.step("Нажать на кнопку поиска"):
            self.driver.find_element(By.CSS_SELECTOR,
                                     'button.header-search__button').click()

    @allure.step("Задать значение: {term}")
    def quantity_ui(self, term: int):
        """
            Эта функция очищает поле для ввода
            и задает количество книг
        """
        quantity = self.driver.find_element(By.CSS_SELECTOR,
                                            "input.product-quantity__counter")
        with allure.step("Очистить поле ввода"):
            quantity.clear()
        with allure.step("Внести количество книг в поле ввода"):
            quantity.send_keys(term)
