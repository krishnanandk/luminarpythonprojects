# def add(*args):
#     sum=0
#     for num in args:             #ags-accepted in tuple format
#        sum+=num
#     return sum
#
# res=add(10,20,30,40)
# print(res)



# def print_person_details(*args):
#     print(args)
#
# print_person_details("ajay","tsr","kakkanad")

# lst=[10,15,8,20,23,20]
# lst=sorted(lst,reverse=True)
# print(lst)


# def print_person_details(**kwargs):                                        #dictionary format
#     print(kwargs)
#
# print_person_details(name="ajay",birthplace="tsr",wplace="kakkanad")



# lst=[10,15,8,20,23,20]
# lst=sorted(lst,reverse=True)
# print(lst)





#ques based on the concept

employees={
    1000:{"name":"sajay","desig":"pythontrainer","exp":3},
    1001:{"name":"sabir","desig":"bigdatatrainer","exp":2},
    1002:{"name":"christy","desig":"ml","exp":3}

}

# eid=int(input("enter employee id"))
# if(eid in employees):
#     print(employees[eid]["name"])
# else:
#     print("eid not exist")


#create a function
#print_emp(eid=1000) - #employee name

def emp_details(**kwargs):                 #kwargs={eid:1000}
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("eid not exists")

emp_details(eid=1001,prop="desig")