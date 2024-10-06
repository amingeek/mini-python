n = 3
z = 2**n

for i in range(1,z):
    listz = []
    temp = i
    ozv = 1

    while temp > 0 :
        if temp % 2 == 1:
            listz += [ozv]
        temp = temp // 2
        ozv += 1
    print(listz)