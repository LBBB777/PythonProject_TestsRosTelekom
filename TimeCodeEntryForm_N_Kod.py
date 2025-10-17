import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import datetime
#
import driver

print('______________Проверка №1 в файле TimeCodeEntryForm_N_Kod.py________________________________________')
print(
    "ПРОВЕРКА-1: Негативное тестирование  - ввода кода подтверждения в форме «Подтверждение email» (тест-1).\n"
    "Сценарий:\n"
    "1. Вход на страницу «Вход по временному коду».\n"
    "2. Ввод корректного email.\n"
    "3. Получение кода подтверждения.\n"
    "4. Ввод заведомо некорректного кода в форму  «Подтверждение email».\n"
    "5. Проверка отображения сообщения об ошибке.\n"
    "Цель: верификация корректной обработки невалидного кода подтверждения.\n"
    "Количество тестов — 1."
)
print('==========================================')
def test_invalid_code():
    # Инициализация веб-драйвера Chrome
    driver = webdriver.Chrome()
    try:
        # Открываем целевую страницу Вход по временному коду
        driver.get("https://lk.rt.ru/")
        # Ждем загрузки начальной формы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "card-title"))
        )
        # Находим поле ввода email
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        email_field.clear()
        correct_email = "malilu@yandex.ru"
        email_field.send_keys(correct_email)
        # Находим и нажимаем кнопку "Получить код"
        get_code_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "otp_get_code"))
        )
        get_code_button.click()
        # Ждем загрузки формы подтверждения кода
        # Ждем появления полей для ввода цифр кода
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rt-code-input"))
        )
        # Вводим неверный код
        invalid_code = "123456"
        code_input.send_keys(invalid_code)
        # Ждем появления сообщения об ошибке
        try:
            # Ищем сообщение об ошибке по классу или тексту
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "form-error-message"))
            )
            print(f"Сообщение об ошибке: {error_message.text}")
            print("Тест пройден: система корректно определила некорректный код")

        except Exception as e:
            print("Сообщение об ошибке не найдено")
            print(f"Дополнительная информация: {str(e)}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрываем браузер
        driver.quit()
# Запуск теста
test_invalid_code()
# # Добавляем паузу на 120 секунд
# time.sleep(120)
# #############
print('______________Проверка №2 в файле TimeCodeEntryForm_N_Kod.py________________________________________')
print(
    "ПРОВЕРКА-2 - Негативное тестирование. Проверяется надежность работы системы при вводе невалидных OTP-КОДОВ \n"
    "на странице 'Подтверждение email', на которую пользователь попадает со страницы 'Вход по временному коду'\n"
    "при условии верного введения email в поле ввода логина (тест-1).\n"
    "Количество попыток ввода неверного кода подтверждения - 8 (многократная проверка механизма)\n"
    "ПРОВЕРЯЕТСЯ:\n"
    "1) Корректность обработки неверных OTP-кодов\n"
    "2) Стабильность работы системы при множественных неверных попытках\n"
    "3) Механизм блокировки после превышения допустимого количества попыток\n"
    "4) Отображение сообщений об ошибках\n"
    "6) Корректность работы формы ввода\n"
    "\n"
    "ПАРАМЕТРЫ ТЕСТИРОВАНИЯ:\n"
    "- Максимальное количество попыток: 8\n"
    "- Время ожидания загрузки формы: 5 секунд\n"
    "- Время ожидания элементов: 10 секунд\n"
    "- Пауза между попытками: 2 секунды\n"
    "- Тип тестируемых кодов: случайные 6-значные числа\n"
    "\n"
    "ОЖИДАЕМЫЕ РЕЗУЛЬТАТЫ:\n"
    "1) Появление сообщения об ошибке при вводе неверного кода\n"
    "2) Блокировка после 4-й попытки\n"
    "3) Корректная работа формы ввода\n"
    "4) Отсутствие сбоев при многократных попытках"
)
print('==========================================')
def generate_random_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

def test_multiple_invalid_codes():
    driver = webdriver.Chrome()
    try:
        # Открываем целевую страницу
        driver.get("https://lk.rt.ru/")

        # Ждем загрузки начальной формы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "card-title"))
        )

        # Вводим корректный email
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        email_field.clear()
        correct_email = "malilu@yandex.ru"
        email_field.send_keys(correct_email)

        # Получаем код
        get_code_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "otp_get_code"))
        )
        get_code_button.click()

        # Максимальное количество попыток
        max_attempts = 8
        attempt_count = 0

        while attempt_count < max_attempts:
            try:
                # Каждый раз заново находим элемент ввода кода
                code_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "rt-code-input"))
                )

                # Генерируем случайный код
                random_code = generate_random_code() # # Генерируем новый код
                print(f"\nПопытка {attempt_count + 1}: Вводим код {random_code}")

                # Очищаем поле и вводим новый код
                code_input.clear()
                code_input.send_keys(random_code)   ## Вводим  сгенерированный код  в форму

                # Ждем появления сообщения об ошибке
                error_message = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "form-error-message"))
                )

                print(f"Сообщение об ошибке: {error_message.text}")

                # Проверяем наличие блокировки
                if "Блокировка" in error_message.text:
                    break

                attempt_count += 1

                # Добавляем паузу между попытками
                time.sleep(2)

            except Exception as e:
                print(f"Ошибка на попытке {attempt_count + 1}: {str(e)}")
                break

        if attempt_count == max_attempts:
            print("\nВсе 8 попыток выполнены успешно")
        else:
            print(f"\nБлокировка произошла на попытке {attempt_count + 1}")

    except Exception as e:
        print(f"Произошла критическая ошибка: {str(e)}")
    finally:
        driver.quit()

# Запуск теста
test_multiple_invalid_codes()

# Добавляем паузу на 120 секунд после теста
time.sleep(120)
# ######################################

print('______________Проверка №3 в файле TimeCodeEntryForm_N_Kod.py________________________________________')
print(
    "ПРОВЕРКА-3: Позитивное тестирование отображения формы капчи и её элементов (тестов-7).\n"
    "Сценарий:\n"
    "1. Вход на страницу авторизации (https://lk.rt.ru/).\n"
    "2. Ввод корректного email в поле ввода.\n"
    "3. Запрос кода подтверждения нажатием кнопки «Получить код».\n"
    "4. Ожидание появления формы капчи.\n"
    "5. Проверка наличия всех обязательных элементов формы:\n"
    "   * контейнер формы капчи;\n"
    "   * заголовок формы («Вы не робот?»);\n"
    "   * текстовое описание («Введите символы с картинки для продолжения»);\n"
    "   * изображение капчи;\n"
    "   * поле ввода для ввода символов капчи;\n"
    "   * кнопка «Продолжить» (в неактивном состоянии до ввода капчи).\n"
    "6. Проверка видимости и неактивности кнопки «Продолжить» до заполнения капчи.\n"
    "Цель: верификация корректного отображения и состояния элементов формы капчи, а также соблюдения логики блокировки \n"
    "кнопки «Продолжить» до ввода символов капчи.\n"
    "Количество тестов — 7 (по одному на каждый проверяемый элемент + проверка состояния кнопки)."
)
print('=' * 80)                # print("=" * 80)
def test_captcha_form():
    driver = webdriver.Chrome()
    try:
        # Открываем целевую страницу
        driver.get("https://lk.rt.ru/")

        # Ждем загрузки начальной формы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "card-title"))
        )
        # Ожидание ввода корректного email
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        email_field.clear()
        correct_email = "malilu@yandex.ru"
        email_field.send_keys(correct_email)
        # Получаем код
        get_code_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "otp_get_code"))
        )
        get_code_button.click()

        # Проверяем появление формы капчи
        try:
            # Проверяем появление контейнера формы капчи
            captcha_container = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, "//section[@id='page-right']//div[contains(@class, 'captcha-form-container')]"
                ))
            )
            if captcha_container.is_displayed():
                print("Тест 1: Контейнер формы капчи найден")
            else:
                print("Тест 1: Контейнер формы капчи   не найден")

            # Проверяем наличие заголовка формы
            captcha_title = WebDriverWait(captcha_container, 5).until(
                EC.presence_of_element_located((
                    By.ID, "card-title"
                ))
            )
            if captcha_title.is_displayed():
                print("Тест 2: Заголовок формы с капчей 'Вы не робот?'")
            else:
                print("Тест 2: Заголовок формы c капчей 'Вы не робот?''Вы не робот?' не найден")
            # Проверяем наличие описания
            captcha_description = WebDriverWait(captcha_container, 5).until(
                EC.presence_of_element_located((
                    By.ID, "card-description"
                ))
            )
            if captcha_description.is_displayed():
                print("Тест 3: Описание формы ('Введите символы с картинки для продолжения') найдено! ")
            else:
                print("Тест 3: Описание формы ('Введите символы с картинки для продолжения') не найдено")
            # Проверяем загрузку изображения капчи
            captcha_image = WebDriverWait(captcha_container, 5).until(
                EC.presence_of_element_located((
                    By.CLASS_NAME, "rt-captcha__image"
                ))
            )
            print("Тест 4: Изображение капчи найдено")

            # Проверяем наличие поля ввода капчи
            captcha_input = WebDriverWait(captcha_container, 5).until(
                EC.presence_of_element_located((
                    By.ID, "captcha"
                ))
            )

            print("Тест 5: Поле ввода капчи найдено")
            ###################
            # Проверяем наличие кнопки "Продолжить"
            continue_button = WebDriverWait(captcha_container, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button.rt-btn--orange")
                )
            )
            if "Продолжить" in continue_button.text:
                print("Тест 6: Кнопка «Продолжить» найдена")

                # Проверка видимости и активности кнопки
                if continue_button.is_displayed() and continue_button.is_enabled():
                    print(
                        "Тест 7: ВНИМАНИЕ: Кнопка «Продолжить» видима и активна — тест не успешен, т.к. капча не введена!")
                else:
                    print("Тест 7: Кнопка «Продолжить» НЕ активна, но видна — тест успешен, т.к. капча не введена!")

            else:
                print("Тест 6: провал! Кнопка «Продолжить» не найдена")

                # Итоговое сообщение — исправленный вариант
            print("\nИТОГ тестирования формы капчи:")

            # Проверяем только обязательные элементы (без кнопки «Продолжить»)
            if (captcha_container.is_displayed() and
                    captcha_title.is_displayed() and
                    captcha_description.is_displayed() and
                    captcha_image.is_displayed() and
                    captcha_input.is_displayed()):

                # Дополнительно проверяем, что кнопка _видима_, но _не активна_
                if continue_button.is_displayed() and not continue_button.is_enabled():
                    print(
                        "✅ Все элементы формы капчи найдены и корректны. Кнопка «Продолжить» неактивна (как и ожидалось).")
                else:
                    print("⚠️ Обнаружены проблемы с элементами формы капчи.")

            else:
                print("⚠️ Обнаружены проблемы с элементами формы капчи.")
        # Исключения и finally
        except TimeoutException as e:
            print(f"Ошибка: форма капчи не появилась в течение времени - {str(e)}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {str(e)}")

    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")
    finally:
        driver.quit()
# Запуск теста
test_captcha_form()

#############################################

