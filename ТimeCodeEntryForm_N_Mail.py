import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
import driver
import requests

 # Тестируем ввод одного некорректного email
# print("_______________________Проверка №1 в файле TimeCodeEntryForm_N_Mail.py_____________________________________")
# print(
#     "Проверка №1: негативное тестирование формы «Вход по временному коду».\n"
#     "Цель: проверить, как система обрабатывает некорректный email при попытке получения временного кода.\n"
#     "Состав проверки (2 теста):\n"
#     "— Тест 1: проверка реакции системы на ввод некорректного email — должна отобразиться ошибка валидации.\n"
#     "— Тест 2: проверка точного текста сообщения об ошибке, соответствующего шаблону из документации.\n"
#     "\n"
#     "Предварительные условия:\n"
#     "* Браузер запущен;\n"
#     "* Открыта страница https://lk.rt.ru/;\n"
#     "* Форма «Вход по временному коду» доступна для заполнения.\n"
#     "\n"
#     "Тестовые данные:\n"
#     "* Некорректный email: `testdomain.com` (не содержит символ `@`).\n"
#     "* Ожидаемый текст ошибки: «Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru».\n"
# )
# print("=" * 80)
#
# # Определяем функцию, которая будет содержать весь тестовый сценарий
# def test_invalid_email():
#     driver = webdriver.Chrome()  # Запускаем браузер Chrome
#
#     try:  # Начинаем блок обработки ошибок
#         # Открываем целевую страницу и ждём её полной загрузки
#         driver.get("https://lk.rt.ru/")
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "card-title"))
#         )
#        # Находим поле ввода email и работаем с ним
#         email_field = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "address"))
#         )
#         email_field.clear()  # Очищаем поле ввода (на случай, если там что-то есть)
#         # Задаём некорректный email для тестирования
#         invalid_email = "testdomain.com"
#         email_field.send_keys(invalid_email)  # Вводим некорректный email в поле
#
#         # Находим и нажимаем кнопку «Получить код»
#         get_code_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "otp_get_code"))
#         )
#         get_code_button.click()
#
#         # Ищем сообщение об ошибке после отправки некорректного email
#         error_message = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.ID, "address-meta"))
#         )
#         # Тест 1: проверяем, что система распознала некорректный email
#         if error_message.is_displayed():
#             print("Тест 1: успех! Система корректно определила, что введённый email некорректен и отвергла его.")
#         else:
#             print("Тест 1: провал! Система не распознала некорректный email.")
#
#         # Тест 2: проверяем текст сообщения об ошибке
#         expected_error_text = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
#         if error_message.text == expected_error_text:
#             print(f"Тест 2: успех! Фактическое сообщение соответствует ожидаемому: '{error_message.text}'.")
#         else:
#             print(f"Тест 2: провал! Фактическое сообщение не соответствует ожидаемому. "
#                   f"Получено: '{error_message.text}', ожидалось: '{expected_error_text}'.")
#
#     except Exception as e:  # Обработка ошибок — если что-то пошло не так
#         print(f"Произошла ошибка: {str(e)}")
#
#     finally:  # Гарантированно закрываем браузер после выполнения теста
#         driver.quit()
#
# # Запускаем тест, если файл запущен как основная программа
# if __name__ == "__main__":
#     test_invalid_email()
# ###########
print(
    "_______________________________Проверка №2 в файле TimeCodeEntryForm_N_Mail.py__________________________________")
print(
    "Проверка №2: негативное тестирование формы «Вход по временному коду» (пакет тестов — 11 шт).\n"
    "Цель: проверить, как система обрабатывает различные варианты некорректных email-адресов при попытке получения временного кода.\n"
    "Состав проверки (11 тестов):\n"
    "— Тест №1: проверка реакции системы на пустое поле ввода email.\n"
    "— Тест №2: проверка реакции системы на ввод только цифр (без символа `@` и домена).\n"
    "— Тест №3: проверка реакции системы на ввод строки без символа `@` и домена.\n"
    "— Тест №4: проверка реакции системы на ввод email без домена (только локальная часть и символ `@`).\n"
    "— Тест №5: проверка реакции системы на ввод email без расширения домена.\n"
    "— Тест №6: проверка реакции системы на ввод email с слишком коротким расширением домена.\n"
    "— Тест №7: проверка реакции системы на ввод email с слишком длинным расширением домена.\n"
    "— Тест №8: проверка реакции системы на ввод email, домен которого начинается с точки.\n"
    "— Тест №9: проверка реакции системы на ввод email с двойными точками в домене.\n"
    "— Тест №10: проверка реакции системы на ввод email с цифрами в расширении домена.\n"
    "— Тест №11: проверка реакции системы на ввод email, домен которого заканчивается точкой.\n"
    "\n"
    "Предварительные условия:\n"
    "* Браузер запущен;\n"
    "* Открыта страница https://lk.rt.ru/;\n"
    "* Форма «Вход по временному коду» доступна для заполнения;\n"
    "* Поля ввода и кнопка «Получить код» функциональны.\n"
    "\n"
    "Тестовые данные:\n"
    "* Набор некорректных email-адресов (см. словарь `invalid_emails` в коде теста).\n"
    "* Ожидаемый текст ошибки: «Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru».\n"
    "* Ожидаемое поведение: для каждого некорректного email должно отображаться сообщение об ошибке указанного формата.\n"
)
print("=" * 80)
# Создаём словарь с некорректными email
invalid_emails = {
    "1.пустое поле": "",
    "2.только цифры": "123456",
    "3.без @ и домена": "test",
    "4.без домена": "test@",
    "5.без расширения домена": "test@domain",
    "6.слишком короткое расширение": "test@domain.c",
    "7.слишком длинное расширение": "test@domain.toolongextension",
    "8.домен начинается с точки": "test@.com",
    "9.двойные точки в домене": "test@domain..com",
    "10.цифры в расширении": "test@domain.c0m",
    "11.домен заканчивается точкой": "test@domain.com."
}


def test_invalid_emails():
    # Флаг успешности всех тестов
    all_tests_passed = True
    failed_tests = []
    # Инициализация веб-драйвера Chrome
    driver = webdriver.Chrome()

    try:
        driver.get("https://lk.rt.ru/")
        # Ждём загрузки формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "card-title"))
        )

        # Инициализируем счётчик тестов
        test_number = 1

        # Основной цикл для проверки всех email
        for email_type, email_value in invalid_emails.items():
            email_field = None
            try:
                # Находим поле ввода
                email_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "address"))
                )
                # Очищаем поле
                email_field.clear()
                # Вводим некорректный email
                email_field.send_keys(email_value)
                # Находим кнопку «Получить код»
                get_code_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "otp_get_code"))
                )
                # Нажимаем кнопку «Получить код»
                get_code_button.click()
                # Ищем сообщение об ошибке
                error_message = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "address-meta"))
                )

                expected_error_text = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

                if expected_error_text in error_message.text:
                    print(f"Тест №{test_number} для некорректности вида {email_type} — тест пройден ✅")
                else:
                    print(f"Тест №{test_number} для некорректности вида {email_type} — тест не пройден ⚠️")
                    all_tests_passed = False
                    failed_tests.append(email_type)

                # Увеличиваем счётчик тестов
                test_number += 1

            except Exception as e:
                print(f"Тест №{test_number} для некорректности вида {email_type} — тест не пройден: {str(e)} ⚠️")
                all_tests_passed = False
                failed_tests.append(email_type)
                test_number += 1  # Увеличиваем счётчик даже при ошибке

            # Очищаем поле перед следующим тестом
            email_field.clear()

        # Если все тесты прошли успешно (флаг остался True)
        if all_tests_passed:
            print("\nВсе 11 тестов успешно пройдены! ✅")
        else:
            # Если флаг стал False — показываем, какие тесты не прошли
            print(f"\nНе удалось пройти {len(failed_tests)} тестов: ⚠️")
            for failed_test in failed_tests:
                print(f"- {failed_test}")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)} ⚠️")

    finally:
        # Закрываем браузер
        driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_invalid_emails()