import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
import driver
import requests
import selenium


#
############################################################
def test_dropdown_menu_links_1():
    print(" _______________Проверка №1 в файле Key_1.py _______________________________")
    print(
        "ПРОВЕРКА-1. Оценивается стабильность  работы выпадающего меню на странице 'Ростелеком Ключ для управляющих компаний'.\n"
        "Количество тестов - 2, итераций -5 (многократная проверка механизма)\n"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы механизма открытия/закрытия меню\n"
        "2) Стабильность функционирования при многократных кликах\n"
        "3) Полнота отображения всех пунктов меню (3 элемента)\n"
        "4) Соответствие текста в пунктах меню ожидаемым значениям\n"
        "5) Отсутствие ошибок при повторных открытиях\n"
        "6) Корректность отображения всех элементов интерфейса\n"
        "\n"
        "ПАРАМЕТРЫ ТЕСТИРОВАНИЯ:\n"
        "- Количество итераций: 5\n"
        "- Время ожидания загрузки DOM: 10 секунд\n"
        "- Время ожидания кликабельного элемента: 5 секунд\n"
        "- Время ожидания между действиями: 1 секунда"
    )
    print('=' * 80)
    # Инициализируем драйвер Chrome
    driver = webdriver.Chrome()
    test_passed = True  # Флаг успешности теста
    try:
        # Открываем целевую страницу
        driver.get("https://key.rt.ru/mc/")

        # Максимизируем окно браузера
        # driver.maximize_window()

        # Ждем загрузки страницы и находим кнопку меню
        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='pointer'][contains(text(),'Управляющим компаниям')]"))
        )

        # Количество итераций для проверки
        iterations = 5

        for i in range(iterations):
            try:
                print(f"Итерация {i + 1}")

                # Кликаем по кнопке
                menu_button.click()
                time.sleep(1)  # Ждем открытия меню

                # Проверяем, что меню открылось
                menu_items = WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='all_site_menu']/li/a"))
                )

                # Проверяем количество элементов в меню
                if len(menu_items) != 3:
                    print("Тест 1: Ошибка. Количество элементов в меню не равно 3")
                    test_passed = False  # Устанавливаем флаг в False при ошибке
                else:
                    print("Тест 1: Пройден. Количество элементов в меню 3")

                # Проверяем текст в каждом элементе
                expected_items = ["Застройщикам", "Физическим лицам", "Домофонным компаниям"]
                actual_items = [item.text for item in menu_items]

                if sorted(expected_items) != sorted(actual_items):
                    print("Тест 2: Ошибка. Неверный текст в элементах меню")
                    test_passed = False  # Устанавливаем флаг в False при ошибке
                else:
                    print(
                        "Тест 2: Пройден. Элементы меню 'Застройщикам', 'Физическим лицам', 'Домофонным компаниям' успешно найдены!")

                # Кликаем снова для закрытия меню
                menu_button.click()
                time.sleep(1)  # Ждем закрытия меню

                print(f"Итерация {i + 1} прошла успешно")
                print("===============================================")

            except Exception as e:
                print(f"Ошибка на итерации {i + 1}: {str(e)}")
                test_passed = False  # Устанавливаем флаг в False при ошибке


    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        test_passed = False  # Устанавливаем флаг в False при ошибке
    finally:

        # Закрываем браузер
        driver.quit()
    # Выводим код состояния
    if test_passed:
        print("\nСтатус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nСтатус: 500 Ошибка - Тесты не пройдены")

    #########################################


def test_dropdown_menu_links_2():
    print("________________ Проверка №2 в файле Kye_1.py______________________________________")
    print(
        "ПРОВЕРКА-2. Оценивается корректность  перехода на страницу 'Застройщикам' через главное меню сайта.\n"
        "Количество тестов - 3:\n"
        "1) Тест на успешность перехода по ссылке на страницу 'Застройщикам' в первой вкладке\n"
        "2) Тест на успешность перехода по ссылке на страницу 'Застройщикам' во второй вкладке\n"
        "3) Тест на наличие основного контента на странице\n"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Застройщикам'\n"
        "3) Успешность перехода по ссылке в разных вкладках (изменение URL, загрузка целевой страницы)\n"
        "4) Возможность работы с несколькими вкладками одновременно\n"
        "5) Наличие основного контента на целевой странице\n"
        "6) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "7) Стабильность работы механизма перехода между страницами\n"
        "8) Корректность работы браузера при открытии новых вкладок"
    )
    print("===========================================================================================")
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
            print("Тест 1: Успешный переход на страницу Застройщикам. Первая вкладка открылась!")
            # Проверяем наличие заголовка
            #########################3333333333333
            # СОХРАНЯЕМ HANDLE ТЕКУЩЕЙ ВКЛАДКИ
            first_tab = driver.current_window_handle  # Cохраняем текущий /current handle первой вкладки //
            # current_window_handle — это свойство веб-драйвера, которое возвращает уникальный идентификатор (handle) текущей активной вкладки.
            # handle — это как “имя” или “метка” вкладки, по которой мы можем к ней обращаться.

            # ОТКРЫВАЕМ НОВУЮ ВКЛАДКУ
            driver.execute_script(
                "window.open('https://key.rt.ru/mc');")  # Открытие новой вкладки происходит через JavaScript (execute_script), что не влияет на текущую вкладку
            # execute_script() — метод, который позволяет выполнить JavaScript-код прямо в браузере
            #  window.open() — это JavaScript-метод, который открывает новую вкладку/окно
            time.sleep(2)

            # ПЕРЕКЛЮЧАЕМСЯ НА НОВУЮ ВКЛАДКУ
            driver.switch_to.window(driver.window_handles[1])  # # Переключаемся на вторую вкладку

            # ПОВТОРЯЕМ ПРОЦЕДУРУ ПЕРЕХОДА НА СТРАНИЦУ ЗАСТРОЙЩИКАМ
            try:
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
                    EC.url_changes("https://key.rt.ru/mc"))

                # Проверяем наличие основного контента
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                )
                print(
                    "Тест 2: Успешный переход на страницу Застройщикам. Вторая вкладка с страницей Застройщикам Открылась!")
                print("СПРАВОЧНО:    Проверяем наличие контента на второй вкладке")
                # Проверяем наличие заголовка
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                    )
                    print(
                        "Тест 3: Контент на второй вкладке страницы Застройщикам успешно отобразился: Идентификатор - заголовок 'h'")
                except:
                    print(
                        "Тест 3: Ошибка: контент на второй вкладке страницы Застройщикам не найден: Идентификатор - заголовок 'h'")
                    test_passed = False

                # Возвращаемся на первую вкладку
                driver.switch_to.window(first_tab)

            except Exception as e:
                print(f"Ошибка при открытии второй вкладки: {e}")
                test_passed = False
            #######################
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
        print("\nПроверка -2(3 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка -2(3 теста). Статус: 500 Ошибка - Тесты не пройдены")

    #############################################################################


def test_dropdown_menu_links_3():
    print("________________ Проверка №3 в файле Kye_1.py______________________________________")
    print(
        "ПРОВЕРКА-3. Оценивается корректность перехода на страницу 'Физическим лицам' через главное меню сайта.\n"
        "Количество тестов - 4:\n"
        "1) Тест на корректность открытия выпадающего меню управляющих компаний\n"
        "2) Тест на успешность перехода по ссылке на страницу 'Физическим лицам' в первой вкладке\n"
        "3) Тест на успешность перехода по ссылке на страницу 'Физическим лицам' во второй вкладке\n"
        "4) Тест на наличие основного контента на странице во второй вкладке\n"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Физическим лицам'\n"
        "3) Успешность перехода по ссылке в разных вкладках (изменение URL, загрузка целевой страницы)\n"
        "4) Возможность работы с несколькими вкладками одновременно\n"
        "5) Наличие основного контента на целевой странице\n"
        "6) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "7) Стабильность работы механизма перехода между страницами\n"
        "8) Корректность работы браузера при открытии новых вкладок\n"
        "9) Целостность отображения контента при работе с разными вкладками\n"
        "10) Стабильность работы интерфейса при последовательных действиях")
    print("=" * 80)
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
        # Тест 1: Проверка открытия меню
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
        # Проверяем наличие меню
        try:
            # Используем find_elements вместо устаревшего find_elements_by_css_selector
            all_menu_sites = driver.find_elements(By.CSS_SELECTOR, "ul.all_site_menu")

            if all_menu_sites:
                print("Тест 1: Выпадающее меню после клика по кнопке Управляющим компаниям успешно открылось!")

                #  # Тест 2: Переход на страницу Физическим лицам
                try:
                    # Находим ссылку Физическим лицам
                    Individuals = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Физическим лицам')]"))
                    )
                    # Кликаем по ссылке
                    Individuals.click()
                    time.sleep(2)

                    # Ждем загрузки новой страницы  Физическим лицам
                    WebDriverWait(driver, 15).until(
                        EC.url_changes("https://key.rt.ru/mc")
                        # Проверяем изменение с начальной страницы  # 1. Мы проверяем изменение с начальной страницы #  Метод url_changes проверяет именно изменение с исходного URL
                    )
                    # Проверяем наличие основного контента
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                    )
                    print("Тест 2: Успешный переход на страницу Физическим лицам. Первая вкладка открылась!")
                    # Проверяем наличие заголовка
                    #########################
                    # СОХРАНЯЕМ HANDLE ТЕКУЩЕЙ ВКЛАДКИ
                    first_tab = driver.current_window_handle  # Cохраняем текущий /current handle первой вкладки //
                    # current_window_handle — это свойство веб-драйвера, которое возвращает уникальный идентификатор (handle) текущей активной вкладки.
                    # handle — это как “имя” или “метка” вкладки, по которой мы можем к ней обращаться.
                    # Тест 3: Проверка работы во второй вкладке
                    # ОТКРЫВАЕМ НОВУЮ ВКЛАДКУ
                    driver.execute_script(
                        "window.open('https://key.rt.ru/mc');")  # Открытие новой вкладки происходит через JavaScript (execute_script), что не влияет на текущую вкладку
                    # execute_script() — метод, который позволяет выполнить JavaScript-код прямо в браузере
                    #  window.open() — это JavaScript-метод, который открывает новую вкладку/окно
                    time.sleep(2)

                    # ПЕРЕКЛЮЧАЕМСЯ НА НОВУЮ ВКЛАДКУ
                    driver.switch_to.window(driver.window_handles[1])  # # Переключаемся на вторую вкладку

                    # ПОВТОРЯЕМ ПРОЦЕДУРУ ПЕРЕХОДА НА СТРАНИЦУ Физическим лицам
                    try:
                        # Ждем загрузки основной структуры
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "section.top"))
                        )

                        # Находим и открываем меню управляющих компаний
                        menu_button = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
                        )
                        menu_button.click()
                        time.sleep(2)

                        # Ждем появления выпадающего меню
                        WebDriverWait(driver, 15).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.all_site_menu"))
                        )

                        # Находим ссылку Физическим лицам
                        Individuals = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Физическим лицам')]"))
                        )
                        # Кликаем по ссылке
                        Individuals.click()
                        time.sleep(2)
                        # Ждем загрузки новой страницы.  Проверяем изменение с начальной страницы
                        # Начальная страница для второй вкладки тоже https://key.rt.ru/mc
                        # Метод url_changes проверяет именно изменение с исходного URL
                        WebDriverWait(driver, 15).until(
                            EC.url_changes("https://key.rt.ru/mc"))

                        # Проверяем наличие основного контента
                        WebDriverWait(driver, 15).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                        )
                        print("Тест 3: Успешный переход на страницу Физическим лицам во второй вкладке")
                        print("СПРАВОЧНО:    Проверяем наличие контента на второй вкладке")
                        # Проверяем наличие заголовка
                        try:
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                            )
                            print(
                                "Тест 4: Контент на второй вкладке страницы Физическим лицам успешно отобразился: Идентификатор - заголовок 'h'")
                        except:
                            print(
                                "Тест 4: Ошибка: контент на второй вкладке страницы Физическим лицам не найден: Идентификатор - заголовок 'h'")
                            test_passed = False

                        # Возвращаемся на первую вкладку
                        driver.switch_to.window(first_tab)

                    except Exception as e:
                        print(f"Тест 3: Ошибка при работе со второй вкладкой Физическим лицам: {str(e)}")
                        test_passed = False
                    #######################
                except Exception as e:
                    print(f"Тест 2: Ошибка при переходе на страницу Физическим лицам: {e}")
                    test_passed = False  # Устанавливаем флаг в False при ошибке
            else:
                print("Тест 1: Меню после клика по кнопке Управляющим компаниям не открылось.")
                test_passed = False
        except Exception as e:
            print(f"Ошибка при проверке меню: {e}")
            test_passed = False

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
        print("\nПроверка -3(4 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка -3(4 теста). Статус: 500 Ошибка - Тесты не пройдены")
    ######################################################################################


def test_dropdown_menu_links_4():
    print("________________ Проверка №4 в файле Kye_1.py______________________________________")
    print(
        "ПРОВЕРКА-4. Оценивается корректность перехода на страницу 'Домофонным компаниям' через главное меню сайта.\n"
        "Количество тестов - 4:\n"
        "1) Тест на корректность открытия выпадающего меню управляющих компаний\n"
        "2) Тест на успешность перехода по ссылке на страницу 'Домофонным компаниям' в первой вкладке\n"
        "3) Тест на успешность перехода по ссылке на страницу 'Домофонным компаниям' во второй вкладке\n"
        "4) Тест на наличие основного контента на странице во второй вкладке\n"
        "ПРОВЕРЯЕТСЯ:\n"
        "1) Корректность работы навигационного меню (открытие выпадающего списка при клике)\n"
        "2) Доступность и кликабельность ссылки 'Домофонным компаниям'\n"
        "3) Успешность перехода по ссылке в разных вкладках (изменение URL, загрузка целевой страницы)\n"
        "4) Возможность работы с несколькими вкладками одновременно\n"
        "5) Наличие основного контента на целевой странице\n"
        "6) Корректность отображения ключевых элементов (наличие заголовка страницы)\n"
        "7) Стабильность работы механизма перехода между страницами\n"
        "8) Корректность работы браузера при открытии новых вкладок\n"
        "9) Целостность отображения контента при работе с разными вкладками\n"
        "10) Стабильность работы интерфейса при последовательных действиях")
    print("=" * 80)
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
        # Тест 1: Проверка открытия меню
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
        # Проверяем наличие меню
        try:
            # Используем find_elements вместо устаревшего find_elements_by_css_selector
            all_menu_sites = driver.find_elements(By.CSS_SELECTOR, "ul.all_site_menu")

            if all_menu_sites:
                print("Тест 1: Выпадающее меню после клика по кнопке Управляющим компаниям успешно открылось!")

                #  # Тест 2: Переход на страницу Ростелеком Ключ | Домофонным компаниям
                try:
                    # Находим ссылку Ростелеком Ключ | Домофонным компаниям // intercom companies
                    intercom_companies = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//ul[@class='all_site_menu']/li/a[contains(text(), 'Домофонным компаниям')]"))
                    )
                    # Кликаем по ссылке
                    intercom_companies.click()
                    time.sleep(2)

                    # Ждем загрузки новой страницы  Домофонным компаниям, т.е  проверяем процесс перехода
                    WebDriverWait(driver, 15).until(
                        EC.url_changes("https://key.rt.ru/mc")
                        # Проверяем изменение с начальной страницы  # 1. Мы проверяем изменение с начальной страницы на новую #  Метод url_changes проверяет именно изменение с исходного URL
                    )
                    # Проверяем наличие основного контента на той страницена которую перешли
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                    )
                    print(
                        "Тест 2: Успешный переход на страницу Домофонным компаниям. Первая вкладка открылась! Наличе основного контента определено по 'body' ")
                    # Проверяем наличие заголовка
                    #########################
                    # СОХРАНЯЕМ HANDLE ТЕКУЩЕЙ ВКЛАДКИ
                    first_tab = driver.current_window_handle  # Cохраняем текущий /current handle первой вкладки //
                    # current_window_handle — это свойство веб-драйвера, которое возвращает уникальный идентификатор (handle) текущей активной вкладки.
                    # handle — это как “имя” или “метка” вкладки, по которой мы можем к ней обращаться.

                    # Тест 3: Проверка работы во второй вкладке
                    # ОТКРЫВАЕМ НОВУЮ ВКЛАДКУ
                    driver.execute_script(
                        "window.open('https://key.rt.ru/mc');")  # Открытие новой вкладки происходит через JavaScript (execute_script),
                    # что не влияет на текущую вкладку
                    # execute_script() — метод, который позволяет выполнить JavaScript-код прямо в браузере
                    #  window.open() — это JavaScript-метод, который открывает новую вкладку/окно
                    time.sleep(2)

                    # ПЕРЕКЛЮЧАЕМСЯ НА НОВУЮ ВКЛАДКУ
                    driver.switch_to.window(driver.window_handles[1])  # # Переключаемся на вторую вкладку

                    # ПОВТОРЯЕМ ПРОЦЕДУРУ ПЕРЕХОДА НА СТРАНИЦУ Домофонным компаниям
                    try:
                        # Ждем загрузки основной структуры
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "section.top"))
                        )

                        # Находим и открываем меню управляющих компаний
                        menu_button = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, "section.top .left .all_site li.open span.pointer"))
                        )
                        menu_button.click()
                        time.sleep(2)

                        # Ждем появления выпадающего меню
                        WebDriverWait(driver, 15).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.all_site_menu"))
                        )

                        # Находим ссылку Домофонным компаниям
                        intercom_companies = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable(
                                (By.XPATH,
                                 "//ul[@class='all_site_menu']/li/a[contains(text(), 'Домофонным компаниям')]"))
                        )
                        # Кликаем по ссылке
                        intercom_companies.click()
                        time.sleep(2)
                        # Ждем загрузки новой страницы.  Проверяем изменение с начальной страницы
                        # Начальная страница для второй вкладки тоже https://key.rt.ru/mc
                        # Метод url_changes проверяет именно изменение с исходного URL
                        WebDriverWait(driver, 15).until(
                            EC.url_changes("https://key.rt.ru/mc"))

                        # Проверяем наличие основного контента
                        WebDriverWait(driver, 15).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                        )
                        print("Тест 3: Успешный переход на страницу Домофонным компаниям во второй вкладке")
                        print("СПРАВОЧНО:    Проверяем наличие контента на второй вкладке")
                        # Проверяем наличие заголовка
                        try:
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                            )
                            print(
                                "Тест 4: Контент на второй вкладке страницы Домофонным компаниям успешно отобразился: Идентификатор - заголовок 'h'")
                        except:
                            print(
                                "Тест 4: Ошибка: контент на второй вкладке страницы Домофонным компаниям не найден: Идентификатор - заголовок 'h'")
                            test_passed = False

                        # Возвращаемся на первую вкладку
                        driver.switch_to.window(first_tab)

                    except Exception as e:
                        print(f"Тест 3: Ошибка при работе со второй вкладкой Домофонным компаниям: {str(e)}")
                        test_passed = False
                    #######################
                except Exception as e:
                    print(f"Тест 2: Ошибка при переходе на страницу Домофонным компаниям: {e}")
                    test_passed = False  # Устанавливаем флаг в False при ошибке
            else:
                print("Тест 1: Меню после клика по кнопке Управляющим компаниям не открылось.")
                test_passed = False
        except Exception as e:
            print(f"Ошибка при проверке меню: {e}")
            test_passed = False

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
        print("\nПроверка -3(4 теста). Статус: 200 OK - Все тесты пройдены успешно")
    else:
        print("\nПроверка -3(4 теста). Статус: 500 Ошибка - Тесты не пройдены")

    print("_" * 80)

    ##################
    # # Запускаем проверки:
    # if __name__ == "__main__":
    #    test_dropdown_menu_1()    # проверка 1
    #    test_dropdown_menu_2() # проверка 2
    #    test_dropdown_menu_3() # проверка 3
    #    test_dropdown_menu_4()# проверка 4


def run_key_1_tests():
    """Запускает все тесты из файла Key_1.py."""
    print("\n=== Запуск проверок из фала Key_1.py ===\n")

    # print("Проверка №1: Оценивается стабильность  работы выпадающего меню на странице 'Ростелеком Ключ для управляющих компаний'.\n"
    #         "Количество тестов - 2, итераций -5 (многократная проверка механизма)")
    test_dropdown_menu_links_1()

    # print("\nПроверка №2: Оценивается корректность  перехода на страницу 'Застройщикам' через главное меню сайта.\n"
    #         "Количество тестов - 3:")
    test_dropdown_menu_links_2()

    # print("\nПроверка №3: Оценивается корректность перехода на страницу 'Физическим лицам' через главное меню сайта.\n"
    #         "Количество тестов - 4:")
    test_dropdown_menu_links_3()

    # print("\nПроверка №4: Оценивается корректность перехода на страницу 'Домофонным компаниям' через главное меню сайта.")
    # test_dropdown_menu_links_4()

    print("\n=== Все проверки Key_1.py завершены ===\n")


if __name__ == "__main__":
    run_key_1_tests()  # Теперь запускаем через «точку входа»

# Создаем словарь ссылок
# menu_links = {
#     "Застройщикам": "https://key.rt.ru/dev/",
#     "Физическим лицам": "https://key.rt.ru/",
#     "Домофонным компаниям": "https://key.rt.ru/dc/"
# }
