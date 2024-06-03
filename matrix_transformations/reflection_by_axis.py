import numpy as np
from matplotlib import pyplot as plt


def axis_reflection(obj, axis):
    reflection_matrix = None
    if axis == 'x':
        reflection_matrix = np.array([
            [1, 0],
            [0, -1]
        ])

    elif axis == 'y':
        reflection_matrix = np.array([
            [-1, 0],
            [0, 1]
        ])

    # множення матриць
    reflected_obj = np.dot(obj, reflection_matrix)

    return reflected_obj


def plot_reflected_matrix(original_obj, rotated_obj):
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
