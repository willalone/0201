def calculate_salary(employee_id, hours_worked, employees):
    employee = next(emp for emp in employees if emp["id"] == employee_id)
    return hours_worked * employee["hourly_rate"]

def calculate_total_payment(timesheet, employees):
    total = 0
    for entry in timesheet:
        employee_id, hours = entry
        total += calculate_salary(employee_id, hours, employees)
    return total
