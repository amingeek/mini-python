last = int(input(" : "))
list1 = []
for j in range(last+1):
    temp = 0
    a = list(str(j))
    a_int = a

    for i in range(len(a)):
        a[i] = int(a[i])

    for x in range(len(a)):
        temp += (a[x] ** (len(a)))

    if temp == j :
        list1.append(j)
        print(j)


print(list1)