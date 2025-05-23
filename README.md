# Thesis_ILF

**Продукт:** Интернет-магазин книг

**Заказчик:** SkyPro

**Сайт:** [Читай-город](https://www.chitai-gorod.ru/)

## Описание продукта
Интернет-магазин книг, в котором удобно искать и покупать книги. Сохранять книги в закладках при авторизации, искать книги в подборках и с определенными фильтрами
:::
Основная функциональность для проверки: *авторизация, поиск книги, покупка книги*
:::

**Используемые библиотеки**
[requests](https://requests.readthedocs.io/en/latest/api/)
[selenium](https://www.selenium.dev/documentation/)

# Работа с автотестами

### Для того, чтобы запустить тесты для формирования отчета, необходимо:
1. Убедиться, что allure установлен на рабочем компьютере
2. Перейти в терминале к рабочей директории, где находятся необходимые тесты. Например,
    'cd lesson_10'
3. Ввести комнаду подключения allure в терминале
    'pip install allure-pytest'
4. Запустить тесты командой
    'python -m pytest --alluredir allure-result',
    где "allure-result" - это отдельная папка в рабочей директории, куда будут падать результаты прогона

### Для того, чтобы просмотреть сформированный отчет, необходимо:
1. Ввести команду в терминале
    'allure serve allure-result',
    где "allure-result" - это папка в рабочей директории, откуда берутся результаты прогона
