a_input = input(' : ')
a_int_input = int(a_input)
a = list(a_input)
a_int = a
temp = 0
for i in range(len(a)):
    a[i] = int(a[i])

for x in range(len(a)):
    temp += (a[x] ** (len(a)))

if temp == a_int_input :
    print('True')
else:
    print('false')

