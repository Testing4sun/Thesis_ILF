import allure
import requests


base_url = "https://web-gate.chitai-gorod.ru"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjkxODk0OTksImlhdCI6MTc0MzQwOTQ3MywiZXhwIjoxNzQzNDEzMDczLCJ0eXBlIjoyMH0.8yC8J5VXRe7hv2trzyaiSi2eikc0pg7XqFPjuyflvQI"

headers = {
            "Authorization": f"Bearer {token}"
        }


@allure.feature("API - тесты")
@allure.title("Поиск по названию на русском языке")
def test_russian_name_API():
    with allure.step("Поиск списка книг с названием {title}"):
        title = "Мастер и маргарита"
        response = requests.get(f"{base_url}/api/v2/search/",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0


@allure.title("Поиск по названию на английском языке")
def test_english_name_API():
    with allure.step("Поиск списка книг с названием {title}"):
        title = "Alice's Adventures in Wonderland"
        response = requests.get(f"{base_url}/api/v2/search",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0


@allure.title("Поиск по названию, содержащему цифры")
def test_number_name_API():
    with allure.step("Поиск списка книг с названием {title}"):
        title = "1984"
        response = requests.get(f"{base_url}/api/v2/search",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0


@allure.title("Поиск с несуществующим названием")
def test_notexisted_name_API():
    with allure.step("Поиск списка книг с названием {title}"):
        title = "vvvvvvvvvvvvvvvv"
        response = requests.get(f"{base_url}/api/v2/search",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0


@allure.title("Поиск с некорректным/пустым названием")
def test_empty_name_API():
    with allure.step("Поиск списка книг с пустым названием"):
        title = "  "
        response = requests.get(f"{base_url}/api/v2/search",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code != 200
        assert response.status_code > 399
        assert response.status_code < 500
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0


@allure.title("Поиск по названию с ошибкой/опечаткой")
def test_typo_name_API():
    with allure.step("Поиск списка книг с названием {title}"):
        title = "мостер и маргариа"
        response = requests.get(f"{base_url}/api/v2/search",
                                headers=headers, params={"phrase": title})
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    with allure.step("Проверка наличия книг в ответе"):
        assert len(response.json()) > 0
