def x(n):
    t = 100
    a = 1/2
    b = t/2
    
    if n >= 1:
        return a*x(n-1)+b
    
    if n == 0:
        return 1

for i in range(0,100):
    print(x(i))