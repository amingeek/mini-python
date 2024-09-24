list1  = [4,10,1,2,5]
temp = 0
for k in range(len(list1)):
    test = 0
    for i in range(len(list1)-1):

        if list1[i] > list1[i+1]:
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
            test = 1
    if test == 0:
        break

print(list1)

# or use sort()