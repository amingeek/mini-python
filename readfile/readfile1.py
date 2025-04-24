with open("data.txt", "r") as data:
    strings = []
    for i in data:
        strings.append(i.split())
    print(strings)