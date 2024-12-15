def tt(n,a,b):
    t = 100
    # a = 1/2
    # b = t/2
    
    if n >= 1:
        return a*tt(n-1,i/10,j/10)+b
    
    if n == 0:
        return 1
x = 0
list1 = []
for k in range(0,100):
    for i in range(0,1000):
        for j in range(0,1000):
            print(x)
            x += 1
            if (tt(k,i/10,j/10)) == 100:
                list1.append(k)
                list1.append(i/10)
                list1.append(j/10)
                list1.append("|")
                
                

print(list1)