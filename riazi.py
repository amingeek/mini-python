n = int(input('Enter number : '))
while n == 0:
    n = int(input('Enter number : '))
if n % 8 == 0:
    print("Ghavi")
elif n % 4 == 0:
    print("motevaset")
elif n % 2 == 0:
    print("zaei")
else:
    print("pooch")

print('END!')