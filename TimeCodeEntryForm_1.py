from gettext import install

import driver
import pip
import requests
#pip install requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



print("________________Проверка №1 в файле TimeCodeEntryForm_1.py______________________________________")
print("Справочно: Тестирую форму 'Вход по временному коду'используя библиотеку Selenium")
print(
    "ПРОВЕРКА-1 ОТОБРАЖЕНИЕ ОСНОВНЫХ ЭЛЕМЕНТОВ ФОРМЫ «ВХОД ПО ВРЕМЕННОМУ КОДУ» (5 тестов).\n"
    "Цель: проверить присутствие и корректность отображения ключевых UI-элементов.\n"
    "Элементы проверки: заголовок, инструкция, кнопки «Получить код», «Войти со своим паролем», «Помощь»."
    "Тестов - 5 штук"
)

print("===========================================================================================")
#  Тест 1
def test_http_response_1():
    print("Начинается HTTP-тест 1")

    # Инициализация драйвера (укажите путь к chromedriver, если не в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get('https://lk.rt.ru/')

        # Добавляем паузу для загрузки контента (можно настроить время)
        time.sleep(10)


        # Ищем элемент по ID
        card_title = driver.find_element(By.ID, 'card-title')
        actual_text = card_title.text.strip()# strip() убирает пробелы по краям
        # Ожидаемый текст
        expected_text = 'Вход по временному коду'
        if expected_text == actual_text:
            print("Тест 1: Текст заголовка формы 'Вход по временному коду' соответствует ожидаемому ")
        else:
            print(f"Тест 1: Текст заголовка формы 'Вход по временному коду' не соответствует ожидаемому")
            print(f"Ожидалось: '{expected_text}'")
            print(f"Фактически: '{actual_text}'")
    finally:
        # Закрываем браузер
        driver.quit()



##########################

#  Тест 2
def test_http_response_2():
    print("Начинается HTTP-тест 2")

    # Инициализация драйвера (укажите путь к chromedriver, если не в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get('https://lk.rt.ru/')

        # Добавляем паузу для загрузки контента (можно настроить время)
        time.sleep(10)

        # Ищем элемент по ID
        card_description = driver.find_element(By.ID, 'card-description')
        actual_text = card_description.text.strip()# strip() убирает пробелы по краям
        # Ожидаемый текст
        expected_text = 'Укажите почту или номер телефона, на которые необходимо отправить код подтверждения'
        if expected_text == actual_text:
            print("Тест 2: Инструкция по заполнению поля ввода соответствует ожидаемой и представляетсобой текст: 'Укажите почту или номер телефона, на которые необходимо отправить код подтверждения'")
        else:
            print(f"Тест 2:  Инструкция по заполнению поля ввода соответствует  не соответствует ожидаемой")
            print(f"Ожидалось: '{expected_text}'")
            print(f"Фактически: '{actual_text}'")
    finally:
        # Закрываем браузер
        driver.quit()


#  Тест 3
def test_http_response_3():
    print("Начинается HTTP-тест 3")

    # Инициализация драйвера (укажите путь к chromedriver, если не в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get('https://lk.rt.ru/')

        # Добавляем паузу для загрузки контента (можно настроить время)
        time.sleep(10)

        # Ищем элемент по ID
        button_get_code = driver.find_element(By.ID, 'otp_get_code')
        actual_text = button_get_code.text.strip()# strip() убирает пробелы по краям
        # Ожидаемый текст
        expected_text = 'Получить код'
        if expected_text == actual_text:
            print("Тест 3: Кнопка  'Получить код' в форме присутствует")
        else:
            print(f"Тест 3:  Кнопка  'Получить код' в форме  отсутствует")
            print(f"Ожидалось: '{expected_text}'")
            print(f"Фактически: '{actual_text}'")
    finally:
        # Закрываем браузер
        driver.quit()



# ###############
#  Тест 4
def test_http_response_4():
    print("Начинается HTTP-тест 4")

    # Инициализация драйвера (укажите путь к chromedriver, если не в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get('https://lk.rt.ru/')

        # Добавляем паузу для загрузки контента (можно настроить время)
        time.sleep(10)

        # Ищем элемент по ID
        standard_auth_btn = driver.find_element(By.ID, 'standard_auth_btn')
        actual_text = standard_auth_btn.text.strip()# strip() убирает пробелы по краям
        # Ожидаемый текст
        expected_text = 'Войти со своим паролем'
        if expected_text == actual_text:
            print("Тест 4: Кнопка  'Войти со своим паролем' в форме присутствует")
        else:
            print(f"Тест 4:  Кнопка  'Войти со своим паролем' в форме  отсутствует")
            print(f"Ожидалось: '{expected_text}'")
            print(f"Фактически: '{actual_text}'")
    finally:
        # Закрываем браузер
        driver.quit()


#########################################
#  Тест 5
def test_http_response_5():
    print("Начинается HTTP-тест 5")

    # Инициализация драйвера (укажите путь к chromedriver, если не в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get('https://lk.rt.ru/')

        # Добавляем паузу для загрузки контента (можно настроить время)
        time.sleep(10)

        # Ищем элемент по ID
        help_btn = driver.find_element(By.ID, 'faq-open')
        actual_text = help_btn.text.strip()# strip() убирает пробелы по краям
        # Ожидаемый текст
        expected_text = 'Помощь'
        if expected_text == actual_text:
            print("Тест 5: Кнопка  'Помощь' в форме присутствует")
        else:
            print(f"Тест 5:  Кнопка  'Помощь' в форме  отсутствует")
            print(f"Ожидалось: '{expected_text}'")
            print(f"Фактически: '{actual_text}'")
    finally:
        # Закрываем браузер
        driver.quit()

print("\n Проверка 1 в составе 5-ти HTTP-тестов завершена")


def run_TimeCodeEntryForm_1_tests():
    """Запускает все тесты из файла TimeCodeEntryForm_1.py."""
    print("\n=== Запуск тестов (5 шт) проверки 1 из фала TimeCodeEntryForm_1.py ===\n")

    test_http_response_1()
    test_http_response_2()
    test_http_response_3()
    test_http_response_4()
    test_http_response_5()

    print("\n=== Все тесты (5 шт) из фала TimeCodeEntryForm_1.py завершены ===\n")


if __name__ == "__main__":
    try:
        run_TimeCodeEntryForm_1_tests()
    except Exception as e:
        print(f"\nКритическая ошибка при выполнении тестов из TimeCodeEntryForm_1.py: {e}")
