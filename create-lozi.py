n = int(input("Enter toll of lozi : ")) 
nstar = (2 * n) - 1
x = -1
mylist = []
mystars = [[' ' for _ in range(nstar)] for _ in range(nstar)]  
p = 0

for k in range(1, n * 2):
    if k <= n:
        mylist.append(k)
    else:
        mylist.append(n + x)
        x -= 1

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
