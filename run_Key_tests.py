from Key_1 import run_key_1_tests
from Key_2 import run_key_2_tests

def main():
    print("=== Запуск всех проверок ===\n")

    # Запускаем тесты из Key_1.py
    print("Запуск тестов из файла Key_1.py...")
    run_key_1_tests()
    print("\n")

    # Запускаем тесты из Key_2.py
    print("Запуск тестов из файла Key_2.py...")
    run_key_2_tests()
    print("\n")

    print("=== Все проверки завершены ===")

if __name__ == "__main__":
    main()