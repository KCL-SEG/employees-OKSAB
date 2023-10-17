"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# employee.py

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class BonusCommissionMixin:
    def __init__(self, bonus):
        self.bonus = bonus

    def get_commission(self):
        return self.bonus


class ContractCommissionMixin:
    def __init__(self, contracts_landed, commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_commission(self):
        return self.contracts_landed * self.commission_per_contract


class SalariedWithBonusEmployee(SalariedEmployee, BonusCommissionMixin):
    def __init__(self, name, monthly_salary, bonus):
        SalariedEmployee.__init__(self, name, monthly_salary)
        BonusCommissionMixin.__init__(self, bonus)

    def get_pay(self):
        return self.monthly_salary + self.get_commission()

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class HourlyWithBonusEmployee(HourlyEmployee, BonusCommissionMixin):
    def __init__(self, name, hourly_rate, hours_worked, bonus):
        HourlyEmployee.__init__(self, name, hourly_rate, hours_worked)
        BonusCommissionMixin.__init__(self, bonus)

    def get_pay(self):
        return (self.hourly_rate * self.hours_worked) + self.get_commission()

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class SalariedWithContractCommissionEmployee(SalariedEmployee, ContractCommissionMixin):
    def __init__(self, name, monthly_salary, contracts_landed, commission_per_contract):
        SalariedEmployee.__init__(self, name, monthly_salary)
        ContractCommissionMixin.__init__(self, contracts_landed, commission_per_contract)

    def get_pay(self):
        return self.monthly_salary + self.get_commission()

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


class HourlyWithContractCommissionEmployee(HourlyEmployee, ContractCommissionMixin):
    def __init__(self, name, hourly_rate, hours_worked, contracts_landed, commission_per_contract):
        HourlyEmployee.__init__(self, name, hourly_rate, hours_worked)
        ContractCommissionMixin.__init__(self, contracts_landed, commission_per_contract)

    def get_pay(self):
        return (self.hourly_rate * self.hours_worked) + self.get_commission()

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


# Create Employee objects
billie = SalariedEmployee("Billie", 4000)
charlie = HourlyEmployee("Charlie", 25, 100)
renee = SalariedWithContractCommissionEmployee("Renee", 3000, 4, 200)
jan = HourlyWithContractCommissionEmployee("Jan", 25, 150, 3, 220)
robbie = SalariedWithBonusEmployee("Robbie", 2000, 1500)
ariel = HourlyWithBonusEmployee("Ariel", 30, 120, 600)

# Test Employee objects
print(billie.get_pay())
print(str(billie))

print(charlie.get_pay())
print(str(charlie))

print(renee.get_pay())
print(str(renee))

print(jan.get_pay())
print(str(jan))

print(robbie.get_pay())
print(str(robbie))

print(ariel.get_pay())
print(str(ariel))

