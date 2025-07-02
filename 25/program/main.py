import os

FILENAME = "workload.txt"

def read_data(filename):
    """Чтение данных из файла"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    records = []
    for line in lines:
        if line.strip() and not line.startswith("#"):
            parts = line.strip().split(";")
            record = {
                "teacher": parts[0],
                "subject": parts[1],
                "plan_hours": int(parts[2]),
                "fact_hours": int(parts[3])
            }
            records.append(record)
    return records

def write_data(filename, records):
    """Запись данных в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Преподаватель;Дисциплина;Часы_по_плану;Часы_факт\n")
        for rec in records:
            line = f"{rec['teacher']};{rec['subject']};{rec['plan_hours']};{rec['fact_hours']}\n"
            f.write(line)

def add_record(filename):
    """Добавить запись о нагрузке"""
    teacher = input("ФИО преподавателя: ")
    subject = input("Дисциплина: ")
    plan_hours = int(input("Часы по плану: "))
    fact_hours = int(input("Часы фактические: "))

    records = read_data(filename)
    records.append({
        "teacher": teacher,
        "subject": subject,
        "plan_hours": plan_hours,
        "fact_hours": fact_hours
    })
    write_data(filename, records)
    print("Запись добавлена.")

def update_fact_hours(filename):
    """Изменить фактические часы"""
    records = read_data(filename)
    print_records(records)
    index = int(input("Введите номер записи для изменения фактических часов: ")) - 1

    if 0 <= index < len(records):
        new_hours = int(input("Новые фактические часы: "))
        records[index]["fact_hours"] = new_hours
        write_data(filename, records)
        print("Фактические часы обновлены.")
    else:
        print("Неверный номер записи.")

def print_records(records):
    """Вывести все записи"""
    print("\nСписок записей:")
    for idx, rec in enumerate(records, start=1):
        print(f"{idx}. {rec['teacher']} — {rec['subject']} — План: {rec['plan_hours']} — Факт: {rec['fact_hours']}")

def compare_workload(filename):
    """Сравнить план и факт, вывести переработку"""
    records = read_data(filename)
    print("\nСравнение плановой и фактической нагрузки:")
    for rec in records:
        delta = rec['fact_hours'] - rec['plan_hours']
        print(f"{rec['teacher']} ({rec['subject']}): переработка {delta} часов")

def main():
    """Главная функция"""
    while True:
        print("\n=== Учебная нагрузка ===")
        print("1. Добавить запись")
        print("2. Изменить фактические часы")
        print("3. Показать все записи")
        print("4. Сравнить план и факт")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_record(FILENAME)
        elif choice == "2":
            update_fact_hours(FILENAME)
        elif choice == "3":
            records = read_data(FILENAME)
            print_records(records)
        elif choice == "4":
            compare_workload(FILENAME)
        elif choice == "5":
            print("Выход.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()