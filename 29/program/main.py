from library import add_record, return_book
from reminder import check_due_today

FILENAME = "library.txt"

def main():
    while True:
        print("\nБиблиотека")
        print("1. Добавить запись о выдаче книги")
        print("2. Вернуть книгу")
        print("3. Проверить напоминание")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            reader = input("Имя читателя: ")
            book = input("Название книги: ")
            issue_date = input("Дата выдачи (ГГГГ-ММ-ДД): ")
            return_date = input("Дата возврата (ГГГГ-ММ-ДД): ")
            add_record(FILENAME, reader, book, issue_date, return_date)
            print("Запись добавлена.")

        elif choice == '2':
            reader = input("Имя читателя: ")
            book = input("Название книги: ")
            return_book(FILENAME, reader, book)
            print("Книга возвращена.")

        elif choice == '3':
            check_due_today(FILENAME)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
