list1 = [1,1,3,5,8,9,11,11,15,16,15,19,19,20,23,20]

list2 = []

for i in list1:
    if not(i in list2):
        list2.append(i)

print(list2)