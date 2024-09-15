x = int(input('x : '))
a = int(input('a : '))
b = int(input('b : '))
for i in range(a, b + 1):
    if i % x == 0:
        print(i)
