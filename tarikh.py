s = int(input('Enter first year : '))
e = int(input('Enter last year : '))
for i in range(s, e):
    for a in range(1,13):
        if a <= 6:
            x = 32
        elif a <= 11:
            x = 31
        else:
            if i in range(1343, 1473):
                if i % 33 == 1 or i % 33 == 5 or i % 33 == 9 or i % 33 == 13 or i % 33 == 17 or i % 33 == 22 or i % 33 == 26 or i % 33 == 30:
                    x = 31
                else:
                    x = 30
            elif i in range(1244, 1343):
                if i % 33 == 1 or i % 33 == 5 or i % 33 == 9 or i % 33 == 13 or i % 33 == 17 or i % 33 == 21 or i % 33 == 26 or i % 33 == 30:
                    x = 31
                else:
                    x = 30
            
        for e in range(1, x):
            print(i,'/',a,'/',e)
