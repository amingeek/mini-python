a = [3]
x = int(input("Enter number you want it : "))

for i in range(1,x):
    a.append((a[-1]+1)*0.25)

print(a)