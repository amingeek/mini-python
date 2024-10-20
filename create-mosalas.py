n = int(input("Enter toll of Mosalas : "))  
nstar = (2 * n) - 1
mylist = []
mystars = [[' ' for _ in range(nstar)] for _ in range(nstar)]
p = 0

for k in range(1, n * 2):
    if k <= n:
        mylist.append(k)

print("mystars = ", mystars)
print("nstar = ", nstar)
print('mylist = ', mylist)

for i in mylist:
    middle = nstar // 2
    start = middle - (i - 1)
    for j in range(i):
        mystars[p][start + 2 * j] = '.'
    p += 1

for line in mystars:
    print("".join(line))
