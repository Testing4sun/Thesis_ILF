import allure
from selenium import webdriver
from pages.ChitaiGorodUI import ChitaiGorodUI
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


@allure.feature("UI - тесты")
@allure.title("Поиск по названию на русском языке")
def test_russian_name_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorodUI(driver)

    book_search.go_to()
    book_search.name_ui('Мастер и Маргарита')

    with allure.step("Убедиться, что в строке поиска отображается название"):
        search = driver.find_element(By.CSS_SELECTOR,
                                     'input.search-form__input search-form__input--search')
        assert 'Мастер и Маргарита' in search.get_attribute("value")

    driver.quit()


@allure.title("Поиск по пустому названию")
def test_empty_name_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorodUI(driver)

    book_search.go_to()
    book_search.name_ui('')

    with allure.step("Убедиться, что поиск не осуществляется"):
        assert AssertionError

    driver.quit()


@allure.title("Добавление книги в корзину на странице поиска")
def test_add_book_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorodUI(driver)

    book_search.go_to()
    book_search.name_ui('Мастер и Маргарита')

    with allure.step("Получить список результатов"):
        books = driver.find_elements(By.CSS_SELECTOR, 'a.product-card__title')
    with allure.step("Убедиться, что список результатов не пустой"):
        assert len(books) > 0

    with allure.step("Нажать на кнопку 'Купить'"):
        driver.find_element(By.CSS_SELECTOR,
                            'div.product-buttons.product-card__actions button.product-buttons__main-action'
                            ).click()
    with allure.step("Убедиться, что кнопка 'Оформить' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[name='Оформить']")
            )
        )
    with allure.step("Нажать на кнопку 'Оформить'"):
        driver.find_element(By.CSS_SELECTOR, "button[name='Оформить']").click()

    bin = driver.find_element(By.CSS_SELECTOR, "div.cart-item__content")
    assert len(bin) > 0

    driver.quit()


@allure.title("Добавление книги в корзину в количестве 10 штук")
def test_add_several_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorodUI(driver)

    book_search.go_to()
    book_search.name_ui('Божественная комедия')

    with allure.step("Получить список результатов"):
        books = driver.find_elements(By.CSS_SELECTOR, 'a.product-card__title')
    with allure.step("Убедиться, что список результатов не пустой"):
        assert len(books) > 0

    with allure.step("Нажать на кнопку 'Купить'"):
        driver.find_element(By.CSS_SELECTOR,
                            'div.product-buttons.product-card__actions button.product-buttons__main-action'
                            ).click()
    with allure.step("Убедиться, что кнопка 'Оформить' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[name='Оформить']")
            )
        )
    with allure.step("Нажать на кнопку 'Оформить'"):
        driver.find_element(By.CSS_SELECTOR, "button[name='Оформить']").click()

    with allure.step("Убедиться, что кнопка 'Оформить' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "input.product-quantity__counter")
            )
        )
    with allure.step("Убедиться, что выбранной книги больше 9 экземпляров"):
        max = driver.find_element(By.CSS_SELECTOR,
                                  "input.product-quantity__counter")
        assert '> 9' in max.get_attribute("max")
    with allure.step("Ввести необходимое количество книг"):
        book_search.quantity_ui(10)

    driver.quit()


@allure.title("Удаление всех книг в корзине через кнопку 'Очистить корзину'")
def test_delete_all_UI():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    book_search = ChitaiGorodUI(driver)

    book_search.go_to()
    book_search.name_ui('Божественная комедия')

    with allure.step("Получить список результатов"):
        books = driver.find_elements(By.CSS_SELECTOR, 'a.product-card__title')
    with allure.step("Убедиться, что список результатов не пустой"):
        assert len(books) > 0

    with allure.step("Нажать на кнопку 'Купить'"):
        driver.find_element(By.CSS_SELECTOR,
                            'div.product-buttons.product-card__actions button.product-buttons__main-action'
                            ).click()
    with allure.step("Убедиться, что кнопка 'Оформить' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[name='Оформить']")
            )
        )
    with allure.step("Нажать на кнопку 'Оформить'"):
        driver.find_element(By.CSS_SELECTOR, "button[name='Оформить']").click()

    with allure.step("Убедиться, что кнопка 'Очистить корзину' прогрузилась"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.delete-many")
            )
        )
    with allure.step("Нажать на кнопку 'Очистить корзину'"):
        driver.find_element(By.CSS_SELECTOR,
                            "span[name='Очистить корзину']").click()

    with allure.step("Убедиться, что корзина очищена"):
        empty_bin = driver.find_element(By.CSS_SELECTOR,
                                        'p.cart-multiple-delete__title')
        assert 'Корзина очищена' in empty_bin.get_attribute("name")

    driver.quit()
