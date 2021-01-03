class Employee:
    employee_num = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'
        Employee.employee_num += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    
    def apply_raise(self):
        self.pay = self.pay * self.annual_raise

    def __repr__(self):
        pass

    def __str__(self):
        pass
    
    @classmethod
    def set_annual_raise(cls, amount):
        cls.annual_raise = amount
        print(cls)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    def __init__(self, first, last, pay, main_lang):
        super().__init__(first, last, pay)
        self.main_lang = main_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    
    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def prin_emp(self):
        for emp in self.employee:
            print('--->', emp.full_name())



# print(Developer.__mro__)
# Employee.is_workday()

#  (first-last-pay)
# emp_4 = Employee.from_string('Ali-Efrati-10000')
# print(emp_4.email)

dev_1 = Developer('Golnoush', 'Haghighat', 5000, 'Python')
dev_2 = Developer('Mehrnoush', 'Haghighat', 4000, 'C#')
# print(dev_1.email)
print(dev_2.main_lang)

mng_1 = Manager('Mehrnoosh', 'Haghighat', 70000, ['Golnoosh', 'Ali'])
print(mng_1.pay)
mng_1.set_annual_raise(1.10)
# print(help(Manager))
mng_1.apply_raise()
print(mng_1.pay)
print(mng_1.employee)
print('-----------------')
print(dev_1.pay)
dev_1.set_annual_raise(1.20)
dev_1.apply_raise()
print(dev_1.pay)

# print(help(Developer))

