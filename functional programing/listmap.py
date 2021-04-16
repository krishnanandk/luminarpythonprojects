lst=[4,2,1,6,7,8]

#output= [3,1,0,7,8,9]
updatelist=[]
# for i in lst:                       #normal approach
#     if(i<5):
#         i-=1
#         updatelist.append(i)
#     else:
#         i+=1
#         updatelist.append(i)
#
# print(updatelist)

result=list(map(lambda num:num-1 if num<5 else num+1,lst))       #functional programming - concise code
print(result)

# if num<5:
#     num-1
#
# else:
#     num+1
