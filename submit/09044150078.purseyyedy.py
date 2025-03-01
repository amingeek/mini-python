import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x**4 + 5*x**2 + 3*x + 10

x = np.linspace(-100, 100, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = -x^4 + 5x^2 + 3x + 10')

plt.show()