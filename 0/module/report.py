def generate_report(employees, timesheet):
    from calculations import calculate_salary, calculate_total_payment
    
    print("Отчет по зарплатам")
    print("==================")
    
    for entry in timesheet:
        employee_id, hours = entry
        employee = next(emp for emp in employees if emp["id"] == employee_id)
        salary = calculate_salary(employee_id, hours, employees)
        
        print(f"{employee['name']}: {hours} часов × {employee['hourly_rate']} руб./час = {salary} руб.")
    
    print("==================")
    total = calculate_total_payment(timesheet, employees)
    print(f"Итого к выплате: {total} руб.")
