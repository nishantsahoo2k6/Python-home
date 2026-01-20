list_1=[1,2,3,4,5,6]
list_2=[4,5,6,7,8,9,10]
list_3=[]
for i in list_1:
    if i not in list_2:
        list_3.append(i)
print(list_3)