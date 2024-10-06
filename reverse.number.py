n = int(input("Enter number : "))

s = 0

zarib = 1

list1 = []

while(n!=0):

    list1.append(n%10)

    n = n//10


list1.reverse()

for i in range(len(list1)):
    s += (list1[i]*zarib)

    zarib = zarib * 10


print(s)