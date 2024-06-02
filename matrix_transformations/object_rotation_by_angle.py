import numpy as np
from matplotlib import pyplot as plt

def rotation(obj, deg):
    deg_radians = np.radians(deg)

    # матриця повороту
    rotation_matrix = np.array([
        [np.cos(deg_radians), -np.sin(deg_radians)],
        [np.sin(deg_radians), np.cos(deg_radians)]
    ])

    # множення матриць
    rotated_obj = np.dot(obj, rotation_matrix)

    return rotated_obj


def plot_rotated_matrix(original_obj, rotated_obj):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(original_obj[:, 0], original_obj[:, 1] )
    plt.fill(original_obj[:, 0], original_obj[:, 1])
    plt.title('Original Object')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.plot(rotated_obj[:, 0], rotated_obj[:, 1])
    plt.fill(rotated_obj[:, 0], rotated_obj[:, 1])
    plt.title('Rotated Object')
    plt.axis('equal')

    plt.show()
