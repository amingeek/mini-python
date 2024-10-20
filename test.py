string = "HelloHelloHello"
temp = ''
shortstr = string[0]
lastword = ''
n = 1

for i in range(len(string)+1):
    for j in range(len(string)):
        temp = string[j+i:j+n]
        print(temp)
    
        if string.count(temp) >= string.count(shortstr):
            shortstr = temp
    n += 1

print(f'short : {shortstr}')
