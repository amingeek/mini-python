def removeDuplicates(x):
    #x = [1,1,1,2,3,3,4]
    n = 0
    removelist = []
    for i in range(len(x)):
        if i != len(x)-1:
            if x[i] == x[i+1]:
                removelist.append(i)

    for j in removelist:
        x.pop(j+n)
        n -= 1
    return x


a = [1,1,2]

removeDuplicates(a)

print(a)