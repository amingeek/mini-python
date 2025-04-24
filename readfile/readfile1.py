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

def writefileSorted(namef, modef, data):
    temp = 0
    while True:
        n = 0
        for i in range(2, len(data)):
            if data[i][0] < data[i-1][0]:
                n += 1
                temp = data[i-1]
                data[i-1] = data[i]
                data[i] = temp
                temp = 0
        if n == 0:
            with open(namef, modef) as outputs:
                result = ""
                for i in range(len(data)):
                    for k in range(len(data[i])):
                        result += data[i][k] + " "
                    result += "\n"
                    
                outputs.write(result)
                outputs.close()
                return data
        n = 0

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

def findByRotbe(rotbe, data):
    cr = data[rotbe]
    return (f"{cr[1]} ba shomare {cr[0]}")
    
    
def main():
    data = openfile("data.txt", "r")
    writefile("outputs.txt", "w", data)
    sortedlist = writefileSorted("outputs_sorted.txt", "w", data)

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
            elif i == 3:
                rotbe = int(input("Enter a rotbe you wannt it : "))
                print(findByRotbe(rotbe, sortedlist))
                return 0

        except:
            print("Enter a valid option")

main()
