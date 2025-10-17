import TimeCodeEntryForm_1
import TimeCodeEntryForm_2
from StreamToLogger import StreamToLogger
# ### Вывод в консоль #############################################################################
# def run_all_tests():
#     print("\n=== Запуск  тестов из файлов TimeCodeEntryForm_1.py и TimeCodeEntryForm_2.py ===\n")
#
#     try:
#         print("\nЗапускаем тесты из TimeCodeEntryForm_1.py...")
#         TimeCodeEntryForm_1.run_TimeCodeEntryForm_1_tests()  # выбираем функцию из TimeCodeEntryForm_1.py
#     except Exception as e:
#         print(f"\nОшибка при выполнении тестов из TimeCodeEntryForm_1.py: {e}")
#
#     try:
#         print("\nЗапускаем тесты из TimeCodeEntryForm_2.py...")
#         TimeCodeEntryForm_2.run_TimeCodeEntryForm_2_tests()  # выбираем функцию из TimeCodeEntryForm_2.py
#     except Exception as e:
#         print(f"\nОшибка при выполнении тестов из TimeCodeEntryForm_2.py: {e}")
#
#
#     print("\n=== Все тесты системы завершены ===\n")
#
# if __name__ == "__main__":
#     run_all_tests()


### Вывод в текстовый файл через логи #############################################################################
# модули для записи логов с временными метками.
import sys
import logging
from datetime import datetime

# 1. Настраиваем логирование
logging.basicConfig(
    filename = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",  # имя файла с отчётом
    format='%(asctime)s - %(levelname)s - %(message)s',  # формат записи
    level=logging.INFO,  # уровень логирования
    datefmt='%Y-%m-%d %H:%M:%S',  # формат даты и времени
    encoding='utf-8'  # добавляем параметр encoding
)
# Перенаправляем вывод
sys.stdout = StreamToLogger(logging.getLogger(), logging.INFO)
sys.stderr = StreamToLogger(logging.getLogger(), logging.ERROR)

def run_all_tests():
    # 2. Записываем начало тестирования
    logging.info("=== Начало тестирования системы ===")

    # 3. Запускаем тесты из первого файла
    try:
        logging.info("Запускаем тесты из TimeCodeEntryForm_1.py...")
        TimeCodeEntryForm_1.run_TimeCodeEntryForm_1_tests()
        logging.info("Тесты из TimeCodeEntryForm_1.py успешно завершены")
    except Exception as e:
        logging.error(f"Ошибка при выполнении тестов из TimeCodeEntryForm_1.py: {e}")

    # 4. Запускаем тесты из второго файла
    try:
        logging.info("Запускаем тесты из TimeCodeEntryForm_2.py...")
        TimeCodeEntryForm_2.run_TimeCodeEntryForm_2_tests()
        logging.info("Тесты из TimeCodeEntryForm_2.py успешно завершены")
    except Exception as e:
        logging.error(f"Ошибка при выполнении тестов из TimeCodeEntryForm_2.py: {e}")

    # 5. Записываем завершение тестирования
    logging.info("=== Тестирование системы завершено ===")


if __name__ == "__main__":
    run_all_tests()


