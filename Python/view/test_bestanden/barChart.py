import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 10])

for i in range(100):
    y = np.random.randint(1000)
    plt.scatter(i/10, y)
    plt.pause(0.5)

plt.show()