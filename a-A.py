upstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lwstr = "abcdefghijklmnopqrstuvwxyz"
string = 'aAbBcCdD'
ustr = ""
for i in range(len(string)):
    if string[i].islower():
        ustr += upstr[lwstr.find(string[i])]
    else:
        ustr += "".join(string[i])
print(ustr)

