ls = "Amin,   hastam,shoma ki hastid,  ha ? ,bogo!, sari bogo !,  !"

shart = 1

while shart == 1:
    ls = ls.replace(",  ", ",")
    ls = ls.replace(", ", ",")

    if ls.find(", ") == -1:
        shart = 0
        
ls = ls.replace(",", ", ")

print(ls)
