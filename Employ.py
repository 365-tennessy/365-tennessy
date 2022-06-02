class employee:
    def __init__(self, name, salary_amount):
        self.name = name
        self.salary_amount = salary_amount
    def att(self):
        print(f"I am{self.name}and I earn{self.salary_amount}ksh per year")
Emp_001= employee('Pascal Miguel',str(2800000))
Emp_001.att() 