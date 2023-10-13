"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary, hourly_wage, hours_worked, bonus_commission, contracts_landed):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission
        self.contracts_landed = contracts_landed

    def get_pay(self):
        contract_pay = 0
        commission = 0

        if self.contract_type == "salary":
            contract_pay = self.salary
        elif self.contract_type == "hourly":
            contract_pay = self.hourly_wage * self.hours_worked

        if self.bonus_commission is not None:
            contract_pay += self.bonus_commission

        if self.contracts_landed is not None:
            commission = self.contracts_landed * self.contracts_landed_commission

        total_pay = contract_pay + commission

        return total_pay

    def __str__(self):
        if self.contract_type == "salary":
            contract_info = f"{self.name} works on a monthly salary of {self.salary}."
        elif self.contract_type == "hourly":
            contract_info = f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour."
        
        if self.bonus_commission is not None:
            contract_info += f" and receives a bonus commission of {self.bonus_commission}."
        
        if self.contracts_landed is not None:
            contract_info += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contracts_landed_commission}/contract."

        return f"{contract_info} Their total pay is {self.get_pay()}."

# Create employee objects
billie = Employee('Billie', 'salary', 4000, None, None, None, None)
charlie = Employee('Charlie', 'hourly', None, 25, 100, None, None)
renee = Employee('Renee', 'salary', 3000, None, None, None, 4)
jan = Employee('Jan', 'hourly', None, 25, 150, None, 3)
robbie = Employee('Robbie', 'salary', 2000, None, None, 1500, None)
ariel = Employee('Ariel', 'hourly', None, 30, 120, 600, None)

# Test the employees
print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))
