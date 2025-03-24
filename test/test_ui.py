import allure
import pytest
import requests
from selenium import webdriver
from auth.ChitaiGorod import ChitaiGorod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


# Название на русском языке
def test_russian_name_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorod(driver)

    book_search.go_to()
    book_search.name_ui('Мастер и Маргарита')

    with allure.step("Убедиться, что в строке поиска отображается указанное название"):
        search = driver.find_element(By.CSS_SELECTOR,
                                 'input.search-form__input search-form__input--search')
        assert 'Мастер и Маргарита' in search.get_attribute("value")
  
    driver.quit()


# Пустое поле (поиск не осуществлен)
def test_russian_name_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorod(driver)

    book_search.go_to()
    response = book_search.name_ui('')

    with allure.step("Убедиться, что поиск не осуществляется"):
        assert response.status_code > 399

    driver.quit()


# Добавление книги в корзину на странице поиска
def test_add_book_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorod(driver)

    book_search.go_to()
    book_search.name_ui('Мастер и Маргарита')

    with allure.step("Получить список результатов"):
        books = driver.find_elements(By.CSS_SELECTOR, 'a.product-card__title')
    with allure.step("Убедиться, что список результатов не пустой"):
        assert len(books) > 0

    with allure.step("Нажать на кнопку 'Купить'"):
        href_to_check = driver.find_element(By.CSS_SELECTOR,
                            'div.product-buttons.product-card__actions button.product-buttons__main-action'
                            ).click
        href = href_to_check.get_attribute("href")
        return href
    with allure.step("Убедиться, что кнопка 'Оформить' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[name='Оформить']")
            )
        )
    with allure.step("Нажать на кнопку 'Оформить'"):
        driver.find_element(By.CSS_SELECTOR, "button[name='Оформить']").click

    bin = driver.find_element(By.CSS_SELECTOR, "div.cart-item__content")
    assert "{href}" in bin.get_attribute("href")

    driver.quit()




# Добавление книги в корзину на странице книги
# Добавление книги в корзину в количестве 10 штук
# Переход на страницу корзины через кнопку "Оформить"
# Переход на страницу книги через главную страницу
# Удаление книги из корзины
# Удаление всех книг в корзине через кнопку "Очистить корзину"

# Вход в систему через главную страницу
# Вход в систему через страницу с результатами поиска
# Вход в систему через корзину
# Вход в систему через страницу книги
# Вход в систему по неверному коду