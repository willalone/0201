# Данные сотрудников
employees = [
    {"id": 1, "name": "Иванов И.И.", "hourly_rate": 500},
    {"id": 2, "name": "Петров П.П.", "hourly_rate": 450},
    {"id": 3, "name": "Сидоров С.С.", "hourly_rate": 550}
]

# Данные табеля учета времени (id сотрудника, часы работы)
timesheet = [
    (1, 160),
    (2, 145),
    (3, 180)
]

# Функция расчета зарплаты
def calculate_salary(employee_id, hours_worked):
    employee = next(emp for emp in employees if emp["id"] == employee_id)
    return hours_worked * employee["hourly_rate"]

# Функция формирования отчета
def generate_report():
    print("Отчет по зарплатам")
    print("==================")
    total_payment = 0
    
    for entry in timesheet:
        employee_id, hours = entry
        employee = next(emp for emp in employees if emp["id"] == employee_id)
        salary = calculate_salary(employee_id, hours)
        total_payment += salary
        
        print(f"{employee['name']}: {hours} часов × {employee['hourly_rate']} руб./час = {salary} руб.")
    
    print("==================")
    print(f"Итого к выплате: {total_payment} руб.")

# Основная программа
if __name__ == "__main__":
    generate_report()
