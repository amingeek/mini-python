n = int(input("Enter toll of lozi : "))  # input user
nstar = (2 * n) - 1
mylist = []
mystars = [[' ' for _ in range(nstar)] for _ in range(nstar)]  # 2D list of spaces
p = 0

# ساختن لیست از اعداد برای تعداد ستاره‌ها در هر خط
for k in range(1, n * 2):
    if k <= n:
        mylist.append(k)

# چاپ اطلاعات برای دیباگ
print("nstar = ", nstar)
print('mylist = ', mylist)

# پر کردن mystars با نقاط، طوری که بین آنها فاصله باشد
for i in mylist:
    middle = nstar // 2  # موقعیت وسط
    start = middle - (i - 1)  # محاسبه اولین نقطه
    for j in range(i):
        mystars[p][start + 2 * j] = '.'  # قرار دادن نقطه با فاصله
    p += 1

# چاپ لوزی نهایی
for line in mystars:
    print("".join(line))
