class Employee:
    def __init__(self, id, name, hourly_rate):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate
    
    def calculate_salary(self, hours):
        return self.hourly_rate * hours

class TimesheetEntry:
    def __init__(self, employee, hours):
        self.employee = employee
        self.hours = hours
    
    def get_salary(self):
        return self.employee.calculate_salary(self.hours)

class Payroll:
    def __init__(self):
        self.employees = []
        self.timesheet = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def add_timesheet_entry(self, employee_id, hours):
        employee = next(emp for emp in self.employees if emp.id == employee_id)
        self.timesheet.append(TimesheetEntry(employee, hours))
    
    def generate_report(self):
        print("Отчет по зарплатам")
        total_payment = 0
        
        for entry in self.timesheet:
            salary = entry.get_salary()
            total_payment += salary
            
            print(f"{entry.employee.name}: {entry.hours} часов × {entry.employee.hourly_rate} руб./час = {salary} руб.")
        
        print(f"Итого к выплате: {total_payment} руб.")

# Основная программа
if __name__ == "__main__":
    payroll = Payroll()
    
    # Добавляем сотрудников
    payroll.add_employee(Employee(1, "Иванов И.И.", 500))
    payroll.add_employee(Employee(2, "Петров П.П.", 450))
    payroll.add_employee(Employee(3, "Сидоров С.С.", 550))
    
    # Добавляем записи табеля
    payroll.add_timesheet_entry(1, 160)
    payroll.add_timesheet_entry(2, 145)
    payroll.add_timesheet_entry(3, 180)
    
    # Формируем отчет
    payroll.generate_report()
