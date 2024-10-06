n = int(input("Enter a number : "))

if n > 20 :
    print("Na mojaz")
    exit()

z = 2**n
password = 0


for i in range(1,z):
    listz = []
    temp = i
    ozv = 1

    while temp > 0 :
        if temp % 2 == 1:
            listz += [ozv]
        temp = temp // 2
        ozv += 1
    summ = sum(listz)

    if summ > 1:
        tedad_magsom = 0
        for x in range(2,int(summ ** 0.5) + 1):
            if summ % x == 0:
                tedad_magsom += 1
                break
        
        if tedad_magsom == 0 and summ != 1:
            password += summ

print(password)