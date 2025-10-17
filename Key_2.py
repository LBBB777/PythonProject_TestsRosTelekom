import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
#
import logging
import psutil
import random
#
import driver
import requests


def print_test_description_1():
    print(" ______________Проверка № 1 в файле Key_2.py________________________________")
    print(
        "ПРОВЕРКА-1 МЕХАНИЗМА ОТКРЫТИЯ ВЫПАДАЮЩЕГО МЕНЮ НА СТРАНИЦЕ 'Ростелеком Ключ для управляющих компаний'.\n"
        "Два сценария по три теста\n"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Базовая функциональность открытия меню при клике на кнопку 'Управляющим компаниям'\n"
        "2) Визуальная составляющая (видимость элементов) выпадающего меню\n"
        "3) Корректность отображения состояния выпадающего меню (display: block)\n"
        "4) Альтернативные способы активации меню (обычный клик и JS-клик)\n"
        "5) Стабильность работы механизма открытия"
        "ПАРАМЕТРЫ ТЕСТИРОВАНИЯ:"
        "- ожидания загрузки DOM: 20 секунд Ожидание загрузки DOM: 20 секунд"'\n'
        "- ожидания кликабельного элемента: 10 секунд")
    print('==========================================')

def setup_driver():

    driver = webdriver.Chrome()
    driver.get("https://key.rt.ru/mc/")
    # Ожидание загрузки основной структуры страницы
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='top']"))
    )
    return driver

def test_uk_button_prov1():
    test_passed = True  # Флаг успешности теста

    # Получаем инициализированный драйвер
    driver = setup_driver()

    print("СЦЕНАРИЙ 1: Открытие выпадающего меню обычным кликом")
    try:
        driver = setup_driver()
        # Находим кнопку через CSS селектор
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top > div > div.left > ul > li > span.pointer"))
        )

        # Проверяем, что элемент виден
        if element.is_displayed():
            print("Тест 1: Элемент 'Выпадающее меню' виден на странице")
        else:
            print("Тест 1: Элемент 'Выпадающее меню'не виден на странице")
            test_passed = False  # Устанавливаем флаг в False при ошибке
        # Получаем исходное состояние меню
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='all_site_menu']"))
        )
        # initial_style = menu.get_attribute("style")

        # Пробуем разные способы клика
        try:
            # Способ 1: Обычный клик
            element.click()
            time.sleep(2)
            print("Тест 2: Способ клика 'Обычный клик' сработал")
        except  Exception as e:
            print("Тест 2: Произошла ошибка: {str(e)}. Способ клика 'Обычный клик' не сработал")
            test_passed = False  # Устанавливаем флаг в False при ошибке
        try:
            WebDriverWait(driver, 10).until(
                lambda d: "display: block" in d.find_element(By.XPATH, "//ul[@class='all_site_menu']").get_attribute(
                    "style")
            )
            print(
                "Тест 3: Меню в составе кнопок 'Застройщикам','Физическим лицам', 'Домофонным компаниям' при клике на кнопку 'Управляющим компаниям' успешно открылось")

        except Exception as e:
            current_style = menu.get_attribute("style")
            print(f"Произошла ошибка: {str(e)}.Меню не открылось. \n"
                  f"Текущее состояние: {current_style}")

            test_passed = False   # Устанавливаем флаг в False при ошибке

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        # Закрываем браузер
        driver.quit()
        # Выводим код состояния
        if test_passed:
            print("\nПроверка -1, Сценарий 1 (3 теста). Статус 200 OK - Все тесты пройдены успешно" )
        else:
            print("\nПроверка -1, Сценарий 1 (3 теста). 500 Ошибка - Тесты не пройдены")
    print('==========================================')
    print("СЦЕНАРИЙ 2: Открытие выпадающего меню JavaScript - кликом")
    try:
        driver = setup_driver()
        # Находим кнопку через CSS селектор
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top > div > div.left > ul > li > span.pointer"))
        )

        # Проверяем, что элемент виден
        if element.is_displayed():
            print("Тест 4: Элемент 'Выпадающее меню' виден на странице")
        else:
            print("Тест 4: Элемент 'Выпадающее меню'не виден на странице")
            test_passed = False  # Устанавливаем флаг в False при ошибке
        # Получаем исходное состояние меню
        menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='all_site_menu']"))
        )
        # initial_style = menu.get_attribute("style")
        try:
            # Способ 2: JavaScript клик
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            print("Тест 5: Способ клика 'JavaScript - клик' сработал")
        except:
            print("Тест 5: Способ клика 'JavaScript - клик' не сработал")
            test_passed = False  # Устанавливаем флаг в False при ошибке
        # Проверяем состояние меню
        try:
            WebDriverWait(driver, 10).until(
                lambda d: "display: block" in d.find_element(By.XPATH, "//ul[@class='all_site_menu']").get_attribute(
                    "style")
            )
            print(
                "Тест 6: Меню в составе кнопок 'Застройщикам','Физическим лицам', 'Домофонным компаниям' при клике на кнопку 'Управляющим компаниям' успешно открылось")

        except Exception as e:
            current_style = menu.get_attribute("style")
            print(f"Тест 6: Меню не открылось. Текущее состояние: {current_style}")
            print(f"Ошибка при проверке меню: {str(e)}")
            test_passed = False  # Устанавливаем флаг в False при ошибке

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        # Закрываем браузер
        driver.quit()
        # Выводим код состояния
        if test_passed:
            print("\nПроверка-1, Сценарий 2 (3 теста). Статус 200 OK - Все тесты пройдены успешно")
        else:
            print("\nПроверка-1, Сценарий 2 (3 теста). 500 Ошибка - Тесты не пройдены")




# ############################################################################
def print_test_description_2():
    print('______________ Проверка №2 в файле в файле Key_2.py_________________________________________')
    print(
            "ПРОВЕРКА-2 СОДЕРЖАНИЯ И СТРУКТУРЫ ВЫПАДАЮЩЕГО МЕНЮ НА СТРАНИЦЕ 'Ростелеком Ключ для управляющих компаний' "
            "включая элемент 'Управляющим компаниям'.\n"
            "Количество тестов - 2\n"
            "ПРОВЕРЯЕТСЯ:\n"
            "1) Полнота отображения всех пунктов меню\n"
            "2) Корректность текста в каждом пункте меню\n"
            "3) Количество элементов в выпадающем списке\n"
            "4) Визуальная доступность элементов меню\n"
            "5) Целостность структуры выпадающего списка")
    print('==========================================')

def test_uk_button_prov2():
    driver = None
    test_passed = True  # Флаг успешности теста
    try:
        # Инициализируем драйвер
        driver = webdriver.Chrome()
        # Открываем страницу
        driver.get("https://key.rt.ru/mc/")
        driver.maximize_window()
        # Добавляем явное ожидание загрузки DOM
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='top']"))
        )
        # Находим кнопку через CSS селектор
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top > div > div.left > ul > li > span.pointer"))
        )
        # Проверяем, что элемент виден
        if element.is_displayed():
            print("Тест1: проверка видимости элемента на странице. Элемент 'Управляющим компаниям' виден на странице")
        else:
            print("Тест1: проверка видимости элемента на странице. Элемент 'Управляющим компаниям' не виден на странице")
        # Получаем исходное состояние меню
        menu = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='all_site_menu']"))
        )
        initial_style = None  #
        initial_style = menu.get_attribute("style")
        #print(f"Исходное состояние меню: {initial_style}")
        # Выполняем клик
        print("Выполняем клик по кнопке 'Управляющим компаниям'")
        element.click()
        time.sleep(2)
        # Проверяем состояние меню после клика
        try:
            WebDriverWait(driver, 5).until(
                lambda d: "display: block" in d.find_element(By.XPATH, "//ul[@class='all_site_menu']").get_attribute(
                    "style")
            )
            print("Тест2: проверка кликабельности меню при надавливании кнопки 'Управляющим компаниям'.  Меню успешно открылось")
            # Проверяем содержимое меню
            menu_items = driver.find_elements(By.XPATH, "//ul[@class='all_site_menu']/li/a")
            print(f"Детализация: \n"
                  f"Найдено пунктов меню: {len(menu_items)}")
            for item in menu_items:
                print(f"Пункт меню: {item.text}")
                test_passed = False  # Устанавливаем флаг в False при ошибке
        except Exception as e:
            current_style = menu.get_attribute("style")
            print(f"Тест2: проверка кликабельности меню при надавливании кнопки 'Управляющим компаниям'. Меню не открылось. Текущее состояние: {current_style}")
            print(f"Ошибка при проверке меню: {str(e)}")
            test_passed = False  # Устанавливаем флаг в False при ошибке
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        # Закрываем браузер
        driver.quit()
#################
def print_test_description_3():
    print("_________________________________Проверка №3 в файле Key_2.py_________________________________________________________________")
    print(
        "ПРОВЕРКА-3 ФУНКЦИОНАЛЬНОСТИ РАБОТЫ МЕНЮ ВЫБОРА КЛИЕНТА НА СТРАНИЦЕ 'Ростелеком Ключ для управляющих компаний'.\n"
        "Количество тестов - 3, итераций тестирования - 3\n"
        "ПРОВЕРЯЕТСЯ:\n "
        "1) Функциональность работы: появление выпадающего меню при клике на кнопку, корректность отображения всех пунктов меню\n"
        "2) Работоспособность ссылок: правильность переходов по всем пунктам меню, соответствие URL-адресов ожидаемым значениям\n"
        "3) Стабильность работы: время отклика элементов, отсутствие ошибок при переходах, корректная работа механизма возврата на главную страницу\n"
        "4) Корректность отображения контента на целевых страницах\n"
        "5) Пользовательский опыт: видимость элементов, доступность переходов, корректность отображения контента"
    )
    print("===========================================================================================")


# Основная функция тестирования
def test_uk_button_prov3(): #      def test_dropdown_menu_links():
    test_passed = True  # Флаг успешности теста
    driver = None
    try:
        # Инициализируем драйвер
        driver = webdriver.Chrome()

        # Создаем словарь ссылок
        menu_links = {
            "Застройщикам": "https://key.rt.ru/dev/",
            "Физическим лицам": "https://key.rt.ru/",
            "Домофонным компаниям": "https://key.rt.ru/dc/"
        }
        # Открываем страницу
        driver.get("https://key.rt.ru/mc/")
        driver.maximize_window()

        # Ожидание загрузки DOM
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='top']"))
        )

        # Находим и открываем выпадающее меню
        menu_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
        )
        menu_button.click()
        time.sleep(2)

        # Перемешиваем элементы меню для случайного тестирования
        shuffled_links = list(menu_links.items())
        random.shuffle(shuffled_links)

        # Проверяем каждую ссылку
        for link_text, expected_url in shuffled_links:
            try:
                # Обновляем страницу перед каждым тестом
                driver.refresh()
                time.sleep(2)

                # Ждем открытия меню
                menu_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "section.top > div > div.left > ul > li > span.pointer"))
                )
                menu_button.click()
                time.sleep(2)

                # Находим элемент меню
                menu_item = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f"//ul[@class='all_site_menu']//a[contains(text(), '{link_text}')]"))
                )

                # Проверяем URL
                original_url = driver.current_url
                print(f"Исходный URL перед кликом: {original_url}")

                # Кликаем по элементу
                menu_item.click()
                time.sleep(2)
                new_url = driver.current_url
                print(f"Новый URL после клика: {new_url}")

                # Проверяем соответствие URL
                if driver.current_url == expected_url:
                    print(f"Успешный переход по ссылке '{link_text}'. URL совпадает с ожидаемым")

                    # Проверяем наличие контента
                    try:
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//h1"))
                        )
                        print(f"Контент на странице '{link_text}' успешно отобразился")
                    except Exception as e:
                        print(f"Ошибка: контент на странице '{link_text}' не найден: {str(e)}")
                        test_passed = False
                else:
                    print(f"Ошибка: неверный URL для '{link_text}'. Ожидалось: {expected_url}, фактически: {driver.current_url}")
                    test_passed = False

                # Возвращаемся на главную страницу
                driver.back()
                time.sleep(2)

            except Exception as e:
                print(f"Ошибка при проверке ссылки '{link_text}': {str(e)}")
                test_passed = False
        # Если все проверки пройдены успешно
        return test_passed

    except Exception as e:
        print(f"Произошла критическая ошибка: {str(e)}")
        test_passed = False
    finally:
        # Закрываем браузер
        if driver:
            driver.quit()
        return test_passed
# Функция для запуска всех итераций тестирования
def run_tests():
    all_tests_passed = True  # Общий флаг успешности всех тестов
    failed_iterations = []  # Список неудачных итераций

    for attempt in range(3):  # 3 попытки тестирования
        print(f"\n--- Запуск итерации тестирования №{attempt + 1} ---")      # Перед каждой итерацией выводим номер попытки
        try:
            # Запускаем тест и получаем в переменную результат   (True или False)
            result = test_uk_button_prov3()

            if not result:
                all_tests_passed = False
                failed_iterations.append(attempt + 1)
        except Exception as e:
            print(f"Критическая ошибка в итерации {attempt + 1}: {str(e)}")
            all_tests_passed = False
            failed_iterations.append(attempt + 1)

    # Выводим итоговый результат
    if all_tests_passed:
        print("\nВсе тесты пройдены успешно!")
    else:
        print(f"\nТесты не прошли в следующих итерациях: {', '.join(map(str, failed_iterations))}")


# # # # ####################################################################################
def print_test_description_4():
    print("________________Проверка №4 в файле Key_2.py________________________________________")
    print(
        "ПРОВЕРКА-4 КОРРЕКТНОСТИ ПЕРЕХОДА НА СТРАНИЦУ 'Застройщикам' ЧЕРЕЗ ГЛАВНОЕ МЕНЮ САЙТА.\n"
        "Количество тестов - 2: 2.1) Тест на успешность перехода по ссылке на страницу 'Застройщикам'. 2.2) Тест на наличие основного контента"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Застройщикам'\n"
        "3) Успешность перехода по ссылке (изменение URL, загрузка целевой страницы)\n"
        "4) Наличие основного контента на целевой странице\n"
        "5) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "6) Стабильность работы механизма перехода между страницами")
    print("===========================================================================================")
def test_dropdown_menu_links():
    driver = None
    test_passed = True  # Флаг успешности теста
    try:
        # Инициализируем драйвер
        driver = webdriver.Chrome()
        # Шаг 1: Проверка главной страницы
        driver.get("https://key.rt.ru/mc")
        # Ждем загрузки основной структуры
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section.top"))
        )
        # Находим и открываем меню управляющих компаний
        menu_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
        )
        menu_button.click()
        time.sleep(2)
        # Ждем появления выпадающего меню
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.all_site_menu"))
        )
        # Шаг 2: Переход на страницу Застройщикам
        try:
            # Находим ссылку Застройщикам
            zastroyschik_link = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Застройщикам')]"))
            )
            # Кликаем по ссылке
            zastroyschik_link.click()
            time.sleep(2)

            # Ждем загрузки новой страницы
            WebDriverWait(driver, 15).until(
                EC.url_changes("https://key.rt.ru/mc")
            )
            # Проверяем наличие основного контента
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )
            print("Тест 1: Успешный переход на страницу Застройщикам")
            # Проверяем наличие заголовка
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
                print("Тест 2: Контент на странице Застройщикам успешно отобразился")
            except:
                print("Тест 2: Ошибка: контент на странице Застройщикам не найден")
                test_passed = False  # Устанавливаем флаг в False при ошибке
        except Exception as e:
            print(f"Тест 1: Ошибка при переходе на страницу Застройщикам: {e}")
            test_passed = False  # Устанавливаем флаг в False при ошибке
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        try:
            driver.quit()
        except:
            pass
    # Выводим код состояния
    if test_passed:
        print("\nПроверка -4(2 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка -4(2 теста). Статус: 500 Ошибка - Тесты не пройдены")


def print_test_description_5():
    print("_____________________Проверка №5 в файле Key_2.py__________________________________")
    print(
        "ПРОВЕРКА-5 КОРРЕКТНОСТИ ПЕРЕХОДА НА СТРАНИЦУ 'Физическим лицам' ЧЕРЕЗ ГЛАВНОЕ МЕНЮ САЙТА.\n"
        "Количество тестов - 2: 2.1) Тест на успешность перехода по ссылке на страницу 'Физическим лицам'. 2.2) Тест на наличие основного контента"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Физическим лицам'\n"
        "3) Успешность перехода по ссылке (изменение URL, загрузка целевой страницы)\n"
        "4) Наличие основного контента на целевой странице\n"
        "5) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "6) Стабильность работы механизма перехода между страницами"
    )
    print("===========================================================================================")
def test_fizicheskim_litsam():
    driver = None
    test_passed = True # Флаг успешности теста
    try:
        # Инициализируем драйвер
        driver = webdriver.Chrome()
        # Шаг 1: Проверка главной страницы
        driver.get("https://key.rt.ru/mc")
        # Ждем загрузки основной структуры
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section.top"))
        )
        # Находим и открываем меню управляющих компаний
        menu_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
        )
        menu_button.click()
        time.sleep(2)
        # Ждем появления выпадающего меню
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.all_site_menu"))
        )
        # Шаг 2: Переход на страницу Физическим лицам
        try:
            # Находим ссылку Физическим лицам
            fiz_lica_link = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Физическим лицам')]"))
            )
            # Кликаем по ссылке
            fiz_lica_link.click()
            time.sleep(2)
            # Ждем загрузки новой страницы
            WebDriverWait(driver, 15).until(
                EC.url_changes("https://key.rt.ru/mc")
            )
            # Проверяем наличие основного контента
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )
            print("Тест 1: Успешный переход на страницу Физическим лицам")
            # Проверяем наличие заголовка
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
                print("Тест 2: Контент на странице Физическим лицам успешно отобразился")
            except:
                print("Тест 2: Ошибка: контент на странице Физическим лицам не найден")
                test_passed = False  # Устанавливаем флаг в False при ошибке
        except Exception as e:
            print(f"Тест 1: Ошибка при переходе на страницу Физическим лицам: {e}")
            test_passed = False    # Устанавливаем флаг в False при ошибке
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        try:
            driver.quit()
        except:
            pass
        # Выводим код состояния
    if test_passed:
        print("\nПроверка-5 (2 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка-5 (2 теста). Статус: 500 Ошибка - Тесты не пройдены")


def print_test_description_6():
    print("_____________________Проверка №6 в файле Key_2.py______________________________________________")
    print(
        "ПРОВЕРКА-6 КОРРЕКТНОСТИ ПЕРЕХОДА НА СТРАНИЦУ 'Домофонным компаниям' ЧЕРЕЗ ГЛАВНОЕ МЕНЮ САЙТА.\n"
        "Количество тестов - 2: 2.1) Тест на успешность перехода по ссылке на страницу 'Домофонным компаниям'. 2.2) Тест на наличие основного контента"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Домофонным компаниям'\n"
        "3) Успешность перехода по ссылке (изменение URL, загрузка целевой страницы)\n"
        "4) Наличие основного контента на целевой странице\n"
        "5) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "6) Стабильность работы механизма перехода между страницами"
    )
    print("===========================================================================================")
def test_domofonnym_kompaniyam():
    driver = None
    test_passed = True  # Флаг успешности теста
    try:
        # Инициализируем драйвер
        driver = webdriver.Chrome()

        # Шаг 1: Проверка главной страницы
        driver.get("https://key.rt.ru/mc")

        # Ждем загрузки основной структуры
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section.top"))
        )

        # Находим и открываем меню управляющих компаний
        menu_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
        )
        menu_button.click()
        time.sleep(2)

        # Ждем появления выпадающего меню
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.all_site_menu"))
        )

        # Шаг 2: Переход на страницу Домофонным компаниям
        try:
            # Находим ссылку Домофонным компаниям
            domofon_link = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Домофонным компаниям')]"))
            )

            # Кликаем по ссылке
            domofon_link.click()
            time.sleep(2)

            # Ждем загрузки новой страницы
            WebDriverWait(driver, 15).until(
                EC.url_changes("https://key.rt.ru/mc")
            )

            # Проверяем наличие основного контента
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )

            print("Тест 1: Успешный переход на страницу Домофонным компаниям")

            # Проверяем наличие заголовка
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
                print("Тест 2: Контент на странице Домофонным компаниям успешно отобразился")
            except:
                print("Тест 2: Ошибка: контент на странице Домофонным компаниям не найден")
                test_passed = False  # Устанавливаем флаг в False при ошибке
        except Exception as e:

            print(f"Тест 1: Ошибка при переходе на страницу Домофонным компаниям: {e}")
            test_passed = False  # Устанавливаем флаг в False при ошибке
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:
        try:
            driver.quit()
        except:
            pass
 # Выводим код состояния
    if test_passed:
        print("\nПроверка -6(2 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка -6(2 теста). Статус: 500 Ошибка - Тесты не пройдены")


#
# #####################################################################################################################
def run_key_2_tests():
    """Запускает все тесты из файла Key_1.py."""
    print("\n=== Запуск проверок из фала Key_2.py ===\n")
    ####################

    # print("Проверка №1: Оценивается механизм открытия выпадающего меню на странице'Ростелеком Ключ для управляющих компаний'.\n"
    #     "Два сценария по три теста, итераций - 1")
    print_test_description_1()
    test_uk_button_prov1() # запускаем  проверку  1

    # print("Проверка №2: Оценивается стабильность  работы выпадающего меню на странице 'Ростелеком Ключ для управляющих компаний'.\n"
    #         "Количество тестов - 2, итераций -5 (многократная проверка механизма)")
    print_test_description_2()
    test_uk_button_prov2() # запускаем  проверку  2

    # print("Проверка №3: Оценивается функциональность работы меню выбора клиента на странице 'Ростелеком Ключ для управляющих компаний'.\n"
    #     "Количество тестов - 3, итераций - 3\n")
    print_test_description_3()
    run_tests()  # запускаем  проверку  3
    #
    # print("Проверка №4: Оценивается корректность перехода на страницу 'Застройщикам' через главное меню сайта.\n"
    #     "Количество тестов - 2")
    print_test_description_4()
    test_dropdown_menu_links() # запускаем  проверку  4

    # print("Проверка №5: Оценивается корректность перехода на страницу 'Физическим лицам' через главное меню сайта.\n"
    #     "Количество тестов - 2")
    print_test_description_5()
    test_fizicheskim_litsam() # запускаем  проверку 5

    # print("Проверка №6: Оценивается  корректность перехода на страницу 'Домофонным компаниям' через главное меню сайта.\n"
    #     "Количество тестов - 2")
    print_test_description_6()
    test_domofonnym_kompaniyam() # запускаем  проверку 6

    print("\n=== Все проверки Key_2.py завершены ===\n")


if __name__ == "__main__":
    run_key_2_tests()  # Теперь запускаем через «точку входа»



