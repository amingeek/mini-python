def check_list(n,list1):
    x = 0
    
    for i in list1:
        if n % i == 0:
            x += 1
            
    if x == len(list1):
        return True
    else:
        return False
    
def check(n):
    i = 1
    while True:
        if check_list(i,n):
            return i
        else:
            i += 1
            
print(check([2,4,8]))