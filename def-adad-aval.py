def key(x):
    n = 0
    for i in range(1,x+1):
        if x % i == 0:
            n += 1
    if n == 2:
        return True
    else:
        return False
    
def keys(a,b):
    l = []
    for i in range(a,b+1):
        if key(i) == True:
            l.append(i)
    return l

print(keys(1,50))