# lst=[1,2,3,4]
# lst2=[10,20]
# squares=[num**2 for num in lst]
# print(squares)
#
# even=[num for num in lst if num%2==0]
# print(even)



lst=[1,2]
lst2=[10,20]
pairs=[(i,j) for i in lst for j in lst2]
print(pairs)