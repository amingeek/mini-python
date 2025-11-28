def load_data(filename):
    result = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            result.append(line.strip().split(' '))
    return result


def print_data(data):
    for row in data:
        print(row[0] + ' : ' + row[1])

def main():
    data = load_data('list.txt')
    print_data(data)

main()