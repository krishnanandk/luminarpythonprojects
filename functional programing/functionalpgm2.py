#map()
#filter()
#reduce()

lst=[10,20,30,21,22,23,24]

# squ=[]                      #normal approach
# for num in lst:
#     res=num**2
#     squ.append(res)
# print(squ)


#map()
#2 arguments
# 1)function
# 2)iterables

# def squ(no):           #mapping method-for applying in all elements
#     return no**2
#
# squares=list(map(squ,lst))
# print(squares)



squares=list(map(lambda no:no**2,lst))        #mapping method-for applying in all elements (functional programming-concise code)
print(squares)