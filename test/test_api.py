import allure
from selenium import webdriver
from test.pages.ChitaiGorodAPI import ChitaiGorodAPI
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Отправить запрос на поиск книги с названием на русском языке
def test_russian_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с введенным названием"):
        response = get_projects_list("Мастер и маргарита")
        assert response.status_code == 200

    driver.quit()


# Отправить запрос на поиск книги с названием на английском языке
def test_english_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с введенным названием"):
        response = get_projects_list("Alice's Adventures in Wonderland")
        assert response.status_code == 200

    driver.quit()


# Отправить запрос на поиск книги с названием, содержащем цифры
def test_number_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с введенным названием"):
        response = get_projects_list("1984")
        assert response.status_code == 200

    driver.quit()


# Отправить запрос на поиск книги с несуществующим названием
def test_notexisted_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с введенным названием"):
        response = get_projects_list("vvvvvvvvvvvvvvvv")
        assert response.status_code == 200

    driver.quit()


# Отправить запрос на поиск книги с некорректным/пустым названием
def test_empty_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с пустым названием"):
        response = get_projects_list("  ")
        assert response.status_code != 200
        assert response.status_code > 399
        assert response.status_code < 500
        assert response.json().get("title") == "Значение не должно быть пустым."

    driver.quit()


# Отправить запрос на поиск книги с ошибкой/опечаткой в названии
def test_typo_name_API():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
                              ).install()))
    ChitaiGorodAPI(driver)

    with allure.step("Поиск списка книг с ошибкой/опечаткой в названии"):
        response = get_projects_list("мостер и маргариа")
        assert response.status_code == 200

    driver.quit()
