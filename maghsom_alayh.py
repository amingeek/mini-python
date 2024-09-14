n = int(input(' : '))
majmo = 0
tedad = 0
for i in range(1, n+1):
    if (n % i) == 0:
        tedad += 1
        majmo += i
        print(i)
print('tedad = ',tedad)
print('majmo',majmo)