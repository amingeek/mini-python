def encryption(string,passkey,alephba):
    alephba = alephba*2
    new_passkey = passkey*(len(string)//len((passkey))+1)
    j = 0
    temp = []
    for i in string:
        if i.isalpha():
            a_index = alephba.index(i)
            key_index = alephba.index(new_passkey[j])
            temp.append(alephba[a_index+key_index])
        if not i.isalpha():
            temp.append(i)
            
        j += 1
    msg = ''.join(temp)
    return msg

def unencryption(string,passkey,alephba):
    alephba = alephba*2
    new_passkey = passkey*(len(string)//len((passkey))+1)
    j = 0
    temp = []
    for i in string:
        if i.isalpha():
            a_index = alephba.index(i)
            key_index = alephba.index(new_passkey[j])
            temp.append(alephba[a_index-key_index])
        if not i.isalpha():
            temp.append(i)
            
        j += 1
    msg = ''.join(temp)
    return msg

ask = int(input("Enter a number you want it : \nEncryption : 1 \nUnencryption : 2\n : "))
if ask == 1:
    string = input("Enter your string : ")
    passkey = input("Enter your key : ")
    alephba = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    encryptionmsg = encryption(string,passkey,alephba)
    print(encryptionmsg)
    
if ask == 2:
    string = input("Enter your string : ")
    passkey = input("Enter your key : ")
    alephba = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    unencryptionmsg = unencryption(string,passkey,alephba)
    print(unencryptionmsg)



