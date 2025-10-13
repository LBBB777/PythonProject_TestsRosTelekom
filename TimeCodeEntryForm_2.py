import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
import driver
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
#

def test_http_response_prov2():
    print("=" * 80)
    print("________________ Проверка №1 в файле TimeCodeEntryForm_2.py______________________________________")
    print(
        "Проверка 1: Тестируется форма «Вход по временному коду» с использованием библиотек Requests и Selenium (3 теста).")

    print(
        "Проверяется функциональная и визуальная работоспособность формы «ВХОД ПО ВРЕМЕННОМУ КОДУ».\n"
        "Цель: верификация корректной загрузки страницы и присутствия ключевых элементов интерфейса.\n"
        "Элементы проверки:\n"
        "1. Доступность сайта и успешность HTTP-соединения (код ответа 200).\n"
        "2. Наличие поля ввода «E-mail или мобильный телефон».\n"
        "3. Наличие кнопки «Получить код»."
    )
    print("=" * 80)

    test_passed = True  # Флаг успешности теста

    try:
        # Тест 1: проверка доступности сайта через requests
        response = requests.get('https://lk.rt.ru/')
        if response.status_code == 200:
            print(
                "Тест 1: успешно пройден! Подтверждена доступность сайта, корректность работы базового HTTP-соединения,\n"
                "базовая загрузка страницы, отсутствие критических ошибок на стороне сервера.\n"
                f"Статус-код: {response.status_code}"
            )
        else:
            print(
                f"Тест 1: ПРОВАЛ. Ошибка подключения.\nПолучен статус-код: {response.status_code}"
            )
            test_passed = False  # Устанавливаем флаг в False при ошибке

    except requests.RequestException as e:
        print(f"Произошла ошибка при выполнении HTTP-запроса: {e}")
        test_passed = False

    # Инициализация драйвера Selenium
    driver = webdriver.Chrome()  # или другой браузер
    driver.get('https://lk.rt.ru/')
    print("_" * 80)

    try:
        # Ожидание загрузки элементов (настройте таймаут под свои нужды)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='rt-input__placeholder']"))
        )

        # Тест 2: проверка поля ввода
        email_placeholder = driver.find_element(By.XPATH, "//span[@class='rt-input__placeholder']").text
        if email_placeholder == "E-mail или мобильный телефон":
            print(
                "Тест 2: успешно пройден! Поле «E-mail или мобильный телефон» в форме «Вход по временному коду» НАЙДЕНО")
        else:
            print("Тест 2: ПРОВАЛ. Поле «E-mail или мобильный телефон» в форме «Вход по временному коду» НЕ НАЙДЕНО")
            test_passed = False  # Устанавливаем флаг в False при ошибке

        print("_" * 80)

        # Тест 3: проверка кнопки «Получить код»
        button = driver.find_element(By.ID, "otp_get_code")
        if button.text == "Получить код":
            print("Тест 3: успешно пройден! «Кнопка Получить Код» в форме «Вход по временному коду» ИМЕЕТСЯ")
        else:
            print("Тест 3: ПРОВАЛ. «Кнопка Получить Код» в форме «Вход по временному коду» ОТСУТСТВУЕТ")
            test_passed = False  # Устанавливаем флаг в False при ошибке
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()  # Закрываем браузер

    # Вывод итогового результата
    if test_passed:
        print("\nВсе тесты пройдены успешно!")
    else:
        print("\nНекоторые тесты не пройдены. Проверьте ошибки.")

##################################################################################################

def check_get_code_button_f2_1():
    print("________________ Проверка №2 в файле TimeCodeEntryForm_2.py______________________________________")
    print("Проверка №2: Проверяется кликабельность кнопки „Получить код“ при введении актуального e-mail (1 тест)\n"
          "Цель: верификация корректной работы кнопки «Получить код» в сценарии с валидным email-адресом —\n "
          "от заполнения поля до перехода на страницу подтверждения.\n"
          "Тип проверяемого сценария: позитивный (с валидными входными данными)\n"
          "ЭТАПЫ:\n"
          "1) открытие страницы входа (https://lk.rt.ru/);\n"
          "2) Ввод конкретного email перед кликом на кнопку — имитация реального пользовательского сценария с заполненным полем;\n"
          "3) Клик по кнопке;\n"
          "4) Проверка наличия заголовка страницы через XPath\n.")
    print("=" * 80)
    driver = webdriver.Chrome()
    print(
        "Начинается тест 1 (проверки 2): Проверяю кликабельность кнопки «Получить код» при введении актуального email.")
    try:
        # Открываем страницу входа
        driver.get("https://lk.rt.ru/")
        # Создаём объект ожидания элементов (ждём до 20 секунд)
        button_wait = WebDriverWait(driver, 20)
        # Ждём появления кнопки и поля ввода
        button_GetCodButton = button_wait.until(
            EC.presence_of_element_located((By.ID, "otp_get_code"))
        )
        input_field = button_wait.until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        # Вводим email и кликаем по кнопке
        input_field.send_keys("malilu@yandex.ru")
        button_GetCodButton.click()

        # Ждём перехода на страницу «Подтверждение email»
        confirmation_email_title = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[@id='card-title' and text()='Подтверждение email']")
            )
        )
        if confirmation_email_title:
            print("Тест 1 успешно пройден: Клик на кнопку «Получить код» переводит пользователя на страницу формы 'Подтверждение email'")
        else:
            print("Ошибка при прохождении теста 1: не удалось перейти на страницу формы 'Подтверждение email'")

    except Exception as e:
        print(f"Ошибка -1  при кликабельности кнопки «Получить код»: {e}")
        driver.save_screenshot("error_screenshot.png")

    finally:
        # Закрываем браузер
        driver.quit()
# Запускаем функцию

##############################################################################################################

def check_get_code_button_f2_2():
    print("_______________________Проверка №3 в файле TimeCodeEntryForm_2.py_____________________________________")
    print(
        "Проверка №3: Проверяется кликабельность кнопки «Получить код» и корректность маршрутизации при пустом поле ввода логина (2 теста).\n"
        "Цель: проверить работоспособность кнопки «Получить код» при пустом поле ввода,\n"
        "а также корректность перехода на страницу «Подтверждение email».\n"
        "Состав проверки:\n"
        "— Тест 1: проверка кликабельности кнопки и базового перехода.\n"
        "— Тест 2: верификация URL после перехода.")
    print("=" * 80)
    driver = webdriver.Chrome()
    try:
        # Тест 1: проверка кликабельности кнопки и базового перехода
        print("\nТест 1. Проверка кликабельности кнопки «Получить код» и перехода на страницу «Подтверждение email»")
        print("-" * 80)

        # Шаг 1: открытие страницы входа
        driver.get("https://lk.rt.ru/")
        print("Шаг 1. Страница входа успешно открыта.")

        # Шаг 2: ожидание появления кнопки
        GetCodButton_wait = WebDriverWait(driver, 20)
        button_GetCodButton = GetCodButton_wait.until(
            EC.presence_of_element_located((By.ID, "otp_get_code"))
        )
        print("Шаг 2. Кнопка «Получить код» обнаружена на странице.")

        # Шаг 3: клик по кнопке
        button_GetCodButton.click()
        print("Шаг 3. Клик по кнопке выполнен.")

        # Шаг 4: проверка перехода по части URL
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("b2c.passport.rt.ru/auth/realms/b2c")
            )
            print("Шаг 4. Переход на страницу «Подтверждение email» осуществлён успешно.")
            print("\nРезультат теста 1: ПРОЙДЕН")
        except TimeoutException:
            print("Шаг 4. Переход на страницу «Подтверждение email» не осуществлён в течение 10 с.")
            print("\nРезультат теста 1: НЕ ПРОЙДЕН")

        # Тест 2: верификация URL после перехода
        print("\nТест 2. Сверка URL новой страницы с ожидаемым значением")
        print("-" * 80)

        current_url = driver.current_url
        expected_url_part = "b2c.passport.rt.ru/auth/realms/b2c"

        if expected_url_part in current_url:
            print(f"Фактический URL («{current_url}») соответствует ожидаемому значению.")
            print("\nРезультат теста 2: ПРОЙДЕН")
        else:
            print(f"Фактический URL («{current_url}») не соответствует ожидаемому значению.")
            print("\nРезультат теста 2: НЕ ПРОЙДЕН")

    except Exception as e:
        print(f"\nПроизошла ошибка при тестировании: {e}")
        print("Общий результат проверки №3: НЕ ПРОЙДЕН из-за непредвиденной ошибки")

    finally:
        driver.quit()
        print("\nЗавершение проверки №3. Браузер закрыт.")


# ###################################################################################

def check_get_code_button_f2_3():
    print("_______________________Проверка №4 в файле TimeCodeEntryForm_2.py_____________________________________")
    print(
        "Проверка №4: Проверяется кликабельность кнопки «Войти со своим паролем» и корректность маршрутизации при переходе на страницу «Авторизация» (2 теста).\n"
        "Цель: проверить работоспособность кнопки «Войти со своим паролем» на форме «Вход по временному коду», "
        "а также убедиться в корректности перехода на страницу «Авторизация».\n"
        "Состав проверки:\n"
        "— Тест 1: проверка кликабельности кнопки «Войти со своим паролем», выполнение клика и переход на страницу «Авторизация».\n"
        "— Тест 2: верификация URL-адреса после перехода — проверка, что пользователь оказался на нужной странице авторизации."
    )
    print("=" * 80)
    driver = webdriver.Chrome()
    try:
        # Тест 1: проверка кликабельности кнопки «Войти со своим паролем»
        print(
            "\nТест 1. Проверка кликабельности кнопки «Войти со своим паролем» формы «Вход по временному коду» и перехода на страницу «Авторизация»"
        )
        print("-" * 80)
        # Шаг 1: открытие страницы входа
        driver.get("https://lk.rt.ru/")
        print("Шаг 1. Страница входа успешно открыта.")
        # Шаг 2: ожидание появления кнопки
        LogWithYourPasswordButton = WebDriverWait(driver,
                                                  20)  # Создаём объект ожидания (WebDriverWait) — это как таймер в тесте.
        #    driver передаёт браузер, за которым нужно следить. Переменная LogWithYourPasswordButton хранит этот «таймер».
        button_LogWithYourPasswordButton = LogWithYourPasswordButton.until(     #.until() — метод, который ждёт, пока не выполнится какое-то условие.
            EC.presence_of_element_located((By.ID, "standard_auth_btn"))        # Внутри скобок указано какое условие нужно ждать: появление кнопки на странице.
        )                                                                       # Результат (найденный элемент — кнопка) сохраняется в переменную
        print("Шаг 2. Кнопка «Войти со своим паролем» обнаружена на странице.")

        # Шаг 3: клик по кнопке
        button_LogWithYourPasswordButton.click()
        print("Шаг 3. Клик по кнопке «Войти со своим паролем» выполнен.")
        # Шаг 4: проверка перехода по части URL
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains(
                    "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate"
                )
            )
            print("Шаг 4. Переход на страницу «Авторизация» осуществлён успешно.")
            print("\nРезультат теста 1: ПРОЙДЕН")
        except TimeoutException:
            print("Шаг 4. Переход на страницу «Авторизация» не осуществлён в течение 10 с.")
            print("\nРезультат теста 1: НЕ ПРОЙДЕН")

        # Тест 2: верификация URL после перехода
        print("\nТест 2. Сверка URL новой страницы с ожидаемым значением")
        print("-" * 80)

        current_url = driver.current_url
        expected_url_part = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate"
        if expected_url_part in current_url:
            print(f"Фактический URL («{current_url}») соответствует ожидаемому значению (части URL).")
            print("\nРезультат теста 2: ПРОЙДЕН")
        else:
            print(f"Фактический URL («{current_url}») не соответствует ожидаемому значению.")
            print("\nРезультат теста 2: НЕ ПРОЙДЕН")

    except Exception as e:
        print(f"\nПроизошла ошибка при тестировании: {e}")
        print("Общий результат проверки №3: НЕ ПРОЙДЕН из‑за непредвиденной ошибки")

    finally:
        driver.quit()
        print("\nЗавершение проверки №3. Браузер закрыт.")

###########################################################################################
def InformElementsPage():
    print("_______________________Проверка №5 в файле TimeCodeEntryForm_2.py_____________________________________")
    print(
        "Проверка №5: Проверяются информационные элементы страницы формы «Вход по временному коду» (3 теста).\n"
        "Цель: убедиться, что на странице корректно отображаются ключевые текстовые элементы — заголовок формы, описание и текст условий.\n"
        "Состав проверки:\n"
        "— Тест 1: проверка заголовка формы («Вход по временному коду»).\n"
        "— Тест 2: проверка текста описания формы («Укажите почту или номер телефона, на которые необходимо отправить код подтверждения»).\n"
        "— Тест 3: проверка текста условий («Нажимая кнопку «Получить код», вы принимаете условия»)."
    )
    print("=" * 80)
    # Инициализация драйвера
    driver = webdriver.Chrome()
    test_passed = True  # Флаг успешности теста
    try:
        # Открываем страницу
        driver.get("https://lk.rt.ru/")
        try:
            # Ждем загрузку страницы максимум 10 секунд
            # Проверка заголовка формы - переменная CardTitle
            CardTitle = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "card-title"))
            )
            # Получаем текст элемента
            actual_title = CardTitle.text
            # Проверяем, соответствует ли текст ожидаемому
            excepted_title = "Вход по временному коду"
            test_passed &= (actual_title == excepted_title)  # Накапливаем результат
            if test_passed:
                print(f"Тест 1: Тест пройден! Загрузившийся заголовок формы '{actual_title}' найден и соответствует ожидаемому '{excepted_title}'")
            else:
                print(f"Тест 1: Тест не пройден! Заголовок формы '{actual_title}' не соответсвует ожидаемому '{excepted_title}'")
            # Проверка описания формы - переменная CardDescription
            CardDescription = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "card-description")))
            # Получаем текст элемента
            actual_description = CardDescription.text
            # Проверяем, соответствует ли текст ожидаемому
            excepted_description = "Укажите почту или номер телефона, на которые необходимо отправить код подтверждения"
            test_passed &= (actual_description == excepted_description) # Накапливаем результат
            if test_passed:
                print(f"Тест 2: Тест пройден! Сообщение для клиента '{actual_description}' найдено \n и соответствует ожидаемому '{excepted_description}'")
            else:
                print(f"Тест 2: Тест не пройден! Сообщение для клиента {actual_description}, \n ожидалось - '{ excepted_description}'")
                test_passed = False

            # Проверка текста условий- переменная (TextConditions) the text of the conditions

            TextConditions = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(), 'Нажимая кнопку «Получить код», вы принимаете условия')]"))            )
            # Получаем текст элемента
            actual_conditions = TextConditions.text
            # Проверяем, соответствует ли текст ожидаемому
            excepted_conditions = "Нажимая кнопку «Получить код», вы принимаете условия"
            test_passed &= (actual_conditions == excepted_conditions)   # Накапливаем результат
            if test_passed:
                print(f"Тест 3: Тест пройден! Сообщение для клиента '{actual_conditions}' найдено и соответствует ожидаемому '{excepted_conditions}'")
            else:
                print(f"Тест 3: Тест не пройден! Сообщение для клиента '{actual_conditions}', получен  текст '{actual_conditions}'.")
                test_passed = False
        except Exception as e:  # Начинается обработка ошибок   "Если произошла ошибка"
            print(f"Ошибка при поиске заголовка: {str(e)}")  # преобразование объекта исключения в строку.
            test_passed = False
    finally:
        driver.quit()

        # Финальное сообщение о статусе всего теста
        if test_passed:
            print("\nОбщий результат: ВСЕ ТЕСТЫ ПРОЙДЕНЫ успешно.")
        else:
            print("\nОбщий результат: ТЕСТЫ НЕ ПРОЙДЕНЫ — обнаружены ошибки.")


def run_TimeCodeEntryForm_2_tests():
    """Запускает все тесты из файла TimeCodeEntryForm_2.py."""
    print("\n=== Запуск тестов (5 шт) проверки 1 из фала TimeCodeEntryForm_2.py ===\n")

    test_http_response_prov2()
    check_get_code_button_f2_1()
    check_get_code_button_f2_2()
    check_get_code_button_f2_3()
    InformElementsPage()
    print("\n=== Все тесты (5 шт) из фала TimeCodeEntryForm_2.py завершены ===\n")

if __name__ == "__main__":
    try:
        run_TimeCodeEntryForm_2_tests()
    except Exception as e:
        print(f"\nКритическая ошибка при выполнении тестов из TimeCodeEntryForm_2.py: {e}")

