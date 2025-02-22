import matplotlib.pyplot as plt
import numpy as np

def create_num(list1, n):
    list2 = np.array([])
    for i in list1:
        list2 = np.append(list2, i**n)
    return list2

xpoints1 = np.array([1, 2, 3, 4])
ypoints1 = create_num(xpoints1, 1)

plt.subplot(2, 2, 1)
plt.plot(xpoints1, ypoints1, marker = 'o', linestyle = 'dashed')


xpoints2 = np.array([1, 2, 3, 4])
ypoints2 = create_num(xpoints2, 2)


plt.subplot(2, 2, 2)
plt.plot(xpoints2, ypoints2, marker = 'D', linestyle = 'dashed')


xpoints3 = np.array([1, 2, 3, 4])
ypoints3 = create_num(xpoints3, 3)

plt.subplot(2, 2, 3)
plt.plot(xpoints3, ypoints3, marker = 'H'	, linestyle = 'dashed')

xpoints4 = np.array([1, 2, 3, 4])
ypoints4 = create_num(xpoints4, 4)


plt.subplot(2, 2, 4)
plt.plot(xpoints4, ypoints4, marker = 'p'	, linestyle = 'dashed')



plt.show()

