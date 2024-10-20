string = "Salam khodavand bar to ! ey momen khoda abababababababab"

find = "abab"

c = 0

shart = False

for i in range(len(string)):
    # print(string[i:(i+len(find))])
    if string[i:(i+len(find))] == find:
        
        i += len(find)
        
        shart = True
        
        c += 1
        
        

if shart:
    
    print(f"be tedade {c} kalame \"{find}\" dar \"{string}\" vojod darad!")
