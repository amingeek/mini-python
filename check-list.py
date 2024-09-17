mylist = [1,1,3,5,8,9,11,11,15,16,15,19,19,20,23,20]
d_list = []
d_list.extend(mylist)

for i in mylist:
    index = 0
    for j in mylist:
        if i == j:
            index += 1

        if index >= 2:
            mylist.remove(j)
            break



print(d_list)
print(mylist)