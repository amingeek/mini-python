ifile = 'input.txt'
def count_palindromes(l, r):
    count = 0
    for num in range(l, r + 1):
        if str(num) == str(num)[::-1]:
            count += 1
    return count

with open('input1.txt', 'r') as ifile:
    print(ifile)
# l = int(input("ابتدای بازه را وارد کنید: "))
# r = int(input("انتهای بازه را وارد کنید: "))

# result = count_palindromes(l, r)
# print(f"تعداد اعداد متقارن در بازه [{l}, {r}] برابر است با: {result}")