import numpy as np
import matplotlib.pyplot as plt

Batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
    [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]
])

Object = np.array([
    [1, 1], [0, 0], [1, 0], [3, 4], [4, 0], [0, 3]
])


def draw_plot(obj1, obj2):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(obj1[:, 0], obj1[:, 1])
    plt.fill(obj1[:, 0], obj1[:, 1])
    plt.title('Batman')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.plot(obj2[:, 0], obj2[:, 1])
    plt.fill(obj2[:, 0], obj2[:, 1])
    plt.title('Object')
    plt.axis('equal')

    plt.show()


draw_plot(Batman, Object)
