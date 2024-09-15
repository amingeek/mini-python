x = 10
a = 0 
b = 1 
list1 = []
for i in range(x+1):
    list1.append(a)
    list1.append(b)
    a += b 
    b += a
print(list1)