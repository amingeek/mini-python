n = int(input("Enter a number : "))

s = 0

list1 = [0]*n

deff = list1.copy()

for i1 in range(n-3):

    for i2 in range(i1+3,n):

        for i3 in range(i1+1, i2-1):
            
            for i4 in range(i3+1,i2):

                list1[i1] = 1
                list1[i2] = 1
                list1[i3] = 1
                list1[i4] = 1

                print(list1)

                list1 = deff.copy()

                s += 1


print(s)
