import numpy as np
import matplotlib.pyplot as plt


def draw_plot(obj1, obj2=None):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(obj1[:, 0], obj1[:, 1])
    plt.fill(obj1[:, 0], obj1[:, 1])
    plt.title('Batman')
    plt.axis('equal')

    if obj2 is not None:
        plt.subplot(1, 2, 2)
        plt.plot(obj2[:, 0], obj2[:, 1])
        plt.fill(obj2[:, 0], obj2[:, 1])
        plt.title('Object')
        plt.axis('equal')

    plt.show()
