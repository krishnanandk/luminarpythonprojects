#reduce()


from functools import reduce              #to imort reduce function


lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)      #2 arguments in lambda in reduce function
print(total)

max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)    #to find maximum number
print(max)




min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)    #to find minimmum number
print(min)

