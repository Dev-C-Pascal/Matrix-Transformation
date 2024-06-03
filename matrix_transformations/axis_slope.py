import numpy as np
from matplotlib import pyplot as plt


# Функція для нахилу об'єкта
def slope(obj, axis, deg):
    slope_matrix = None

    if axis == 'x':
        slope_matrix = np.array([
            [1, deg],
            [0, 1]
        ])
    elif axis == 'y':
        slope_matrix = np.array([
            [1, 0],
            [deg, 1]
        ])

    sheared_obj = np.dot(obj, slope_matrix)

    return sheared_obj


def plot_sloped_matrix(original_obj, rotated_obj):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(original_obj[:, 0], original_obj[:, 1])
    plt.fill(original_obj[:, 0], original_obj[:, 1])
    plt.title('Original Object')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.plot(rotated_obj[:, 0], rotated_obj[:, 1])
    plt.fill(rotated_obj[:, 0], rotated_obj[:, 1])
    plt.title('Rotated Object')
    plt.axis('equal')

    plt.show()
