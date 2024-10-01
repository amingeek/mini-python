a = int(input(' Enter a number : '))
mylist = [a]

while True:
    if a == 1:
        break

    if a % 2 != 0:
        a = ((a *3) +1)
        mylist.append(int(a))

    if a % 2 == 0:
        a = (a / 2)
        mylist.append(int(a))


print(mylist)