for j in range(1000, 10000):
    s = j
    while s != 0 and s != 6174:
        i = 0
        k = 0
        n = s
        zarib = 1
        sx = 0
        sm = 0
        list1 = []

        while n != 0:
            list1.append(n % 10)
            n = n // 10

        list1.sort(reverse=True)
        smax = list1.copy()

        for i in range(len(list1)):
            sx += smax[i] * zarib
            zarib = zarib * 10

        zarib = 1
        list1.sort()
        smin = list1.copy()

        for k in range(len(list1)):
            sm += smin[k] * zarib
            zarib = zarib * 10

        s = sx - sm

    print("j = ", j)
    print(s)
