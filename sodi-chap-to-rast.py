list1 = []
for i in range(1000, 10000):
    a = list(str(i))

    if int(a[0]) < int(a[1]) and int(a[1]) < int(a[2]) and int(a[2]) < int(a[3]):
        list1.append(i)

print(list1)