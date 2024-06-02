import numpy as np


def scale(obj, coef):

    # матриця маштабування
    scaling_matrix = np.array([
        [coef, 0],
        [0, coef]
    ])

    # множення матриць
    scaled_obj = np.dot(obj, scaling_matrix)

    return scaled_obj
