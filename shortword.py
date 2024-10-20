string = 'cd-abcd-abcd-abcd-abcd'
peyda = False
for i in range(1,len(string)):
    short = string[0:i] * (len(string)//i) + string[0:len(string)%i]
    
    if short == string :
        peyda = True
        break
    
if peyda:
    print(f'Vahed tekrari {string[0:i]} ast!')
else:
    print('Vahed tekrari nadarad !')