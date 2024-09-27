list1 = [1,5,8,9,10,9]
list2 = [2,5,9,8,18,9]
list3 = []

for index in list1:

    for index2 in list2:

        if index == index2 and not(index in list3):

            list3.append(index)

            break

print(list3)