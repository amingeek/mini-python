def find_dic(target, dic):
    for i in dic:
        if dic.get(i) == target:
            return i

dic = {1:10, 2:20, 3:30}
target = 10

print(find_dic(target, dic))