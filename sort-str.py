string = "salam   khob   has tid                 ?"

newstr = ""


for i in range(len(string)):
    if string[i] != ' ':
        newstr += string[i]
        
        
    elif string[i] == ' ' and string[i+1] != ' ':
        newstr += string[i]
        
print(newstr)
