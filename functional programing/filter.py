#filter()

# lst=[10,20,30,21,22,23,24]
#
# even=list(filter(lambda num:num%2==0,lst))
# print(even)

lst=["akhil","aravind","akshay","varun","vipin","ram"]
anames=list(filter(lambda name:name[0]=="a",lst))
print(anames)