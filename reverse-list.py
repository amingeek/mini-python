list1 = [10,5,7,4,8,1]
list2 = []

n = len(list1)

for i in range(n):
    list2.append(list1[-1-i])

print(list2)
# or use reverse()
