list1 = [1,5,8,9,10,23]
list2 = [2,5,9,8,18,32]
list3 = []

for index in list1:
    for index2 in list2:
        if index == index2:
            list3.append(index)

print(list3)