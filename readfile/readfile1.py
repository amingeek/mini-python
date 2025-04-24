def openfile(namef, modef):
    with open(namef, modef) as data:
        strings = data.readlines()
        result = []
        for i in strings:
            result.append(i.split())
        data.close()
        return result

def writefile(namef, modef, data):
    with open(namef, modef) as outputs:
        result = ""
        for i in range(len(data)):
            for k in range(len(data[i])):
                result += data[i][k] + " "
            result += "\n"
        outputs.write(result)
        outputs.close()
        
def findByNumber(number, data):
    for i in range(1,len(data)):
        if data[i][0] == number:
            return data[i]
    return "404! not found"

def findByName(name, data):
    for i in range(1,len(data)):
        if data[i][1] == name:
            return data[i]
    return "404! not found"

def main():
    data = openfile("data.txt", "r")
    writefile("outputs.txt", "w", data)

    while True:
        try:
            i = int(input("Find by number or name or find rotbe choice options : \n1 : number\n2 : name\n3 : rotbe\n0 : exit\nEnter your choice : "))
            if i == 0:
                return 0
            elif i == 1:
                number = int(input("Enter number to find it : "))
                print(findByNumber(f"{number}", data))
                return 0
            elif i == 2:
                name = input("Enter name to find it : ")
                print(findByName(name, data))
                return 0

        except:
            print("Enter a valid option")

    

main()
