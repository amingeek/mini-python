a = int(input(' : '))
aval = []
for i in range(1 ,a + 1):
    n = 0
    for x in range(1,i +1):
        if i % x == 0:
            n += 1
            print('i : ',i,'x : ',x)
    if n == 2:
        aval.append(i)


print(aval)