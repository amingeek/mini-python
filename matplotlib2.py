import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(100)
y = np.random.rand(100)
color = np.random.rand(100)


x1 = np.random.rand(100)
y1 = np.random.rand(100)

plt.scatter(x, y, color='blue', alpha=1)
plt.scatter(x1, y1, color='red', alpha=1)

plt.colorbar(label='Color Intensity')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()
plt.show()
