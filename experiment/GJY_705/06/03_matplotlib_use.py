import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 3 * x**2 + 2 * x + 1

x = np.arange(-5, 5, 0.1)
y = func(x)

plt.plot(x, y, label='$y = 3x^2 + 2x + 1$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function $y = 3x^2 + 2x + 1$')
plt.legend()
plt.grid(True)
plt.show()