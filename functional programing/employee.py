class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary


    def print_emp(self):
        print(self.ename)

    def __str__(self):
        return self.desig+self.ename

e1=Employee(1000,"kk","developer",100000)
e2=Employee(1001,"aa","qa",110000)
e3=Employee(1002,"bb","designer",120000)
e4=Employee(1003,"vv","qa",130000)

employees=[]  #employees=[e1,e2,e3,e4]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)

# sal=[]                                            #normal approach to create salary list
# for emp in employees:
#     sal.append(emp.salary)
# print(sal)

salary=list(map(lambda emp:emp.salary,employees))
print(salary)                                         #mapping method to create salary list


highsal=max(salary)                                    #maximum salary
print(highsal)



developer1=list(filter(lambda emp:emp.desig=="qa",employees))

for dev in developer1:
  print(dev)