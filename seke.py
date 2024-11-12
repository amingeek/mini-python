seke = float(input(" : "))
maliat = 0



if seke > 100 and seke <= 500 :
    maliat = (seke - 100) / 10

if seke > 500 and seke <= 1000 :
    seke -= 500
    maliat = (seke / 5) + 40
    
if seke > 1000:
    seke -= 1000
    maliat = (seke * 0.3) + 140





if maliat != 0 :
    print("maliat bayad bedahid")
    print(maliat)
else:
    print("moaf!")
