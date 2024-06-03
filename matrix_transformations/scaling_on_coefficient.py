import numpy as np
from matplotlib import pyplot as plt


def scale(obj, coef):
    # матриця маштабування
    scaling_matrix = np.array([
        [coef, 0],
        [0, coef]
    ])

    # множення матриць
    scaled_obj = np.dot(obj, scaling_matrix)

    return scaled_obj


def plot_scaled_objects(original_obj, scaled_obj):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(original_obj[:, 0], original_obj[:, 1])
    plt.fill(original_obj[:, 0], original_obj[:, 1])
    plt.title('Original Object')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.plot(scaled_obj[:, 0], scaled_obj[:, 1])
    plt.fill(scaled_obj[:, 0], scaled_obj[:, 1])
    plt.title('Scaled Object')
    plt.axis('equal')

    plt.show()
