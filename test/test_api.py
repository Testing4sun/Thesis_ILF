import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Отправить запрос на поиск книги с названием на русском языке. Например, “Мастер и Маргарита“

# Отправить запрос на поиск книги с названием на английском языке. Например, “Alice's Adventures in Wonderland“

# Отправить запрос на поиск книги с названием, содержащем цифры. Например, “1984“

# Отправить запрос на поиск книги с несуществующим названием. Например, “vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv“

# Отправить запрос на поиск книги с некорректным названием. Например, “ “.

# Отправить запрос на поиск книги с ошибкой/опечаткой в названии. Например, “мостер и маргариа”

# Отправить запрос на поиск книги с пустым значением названия

# Отправить запрос на поиск книги с несуществующим id
