import matplotlib.pyplot as pyplot
import numpy as np

x = [1, 4, 5, 8, 9]
y = [0, 4, 5, 7, 10]

plt.scatter(x, y, label='car', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph\nCheck it out')
plt.legend()
plt.show()
