from file_manager import read_data
from datetime import datetime

def check_due_today(filename):
    today = datetime.today().strftime("%Y-%m-%d")
    records = read_data(filename)
    due_today = [r for r in records if r['return_date'] == today]
    if due_today:
        print("Сегодня нужно вернуть книги:")
        for r in due_today:
            print(f"{r['reader']} должен вернуть '{r['book']}' сегодня.")
    else:
        print("Сегодня нет книг с истекающим сроком возврата.")
