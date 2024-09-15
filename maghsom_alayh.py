n = int(input(' : '))
majmo = 0
tedad = 0
for i in range(1, n+1):
    if i <= (int(n/2)) or i == n:
        if (n % i) == 0:
            tedad += 1
            majmo += i
            print(i)
    
print('tedad = ',tedad)
print('majmo',majmo)