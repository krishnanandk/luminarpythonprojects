class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary


    def print_emp(self):
        print(self.ename)

    def __str__(self):
        return self.ename

emp=Employee(1000,"varun","developer",28000)
emp2=Employee(1001,"arun","developer",29000)
print(emp)
