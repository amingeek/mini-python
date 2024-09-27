a = int(input('Enter a number : '))
mylist = [a]
n = 0
for i in range(a*3):
    if a == 1:
        break

    elif a % 2 == 0:
        a = (a / 2)
        mylist.append(int(a))

    else:
        a = ((a *3) +1)
        mylist.append(int(a))
        
    n += 1

        

print('number of loop = ',n)
print(mylist)