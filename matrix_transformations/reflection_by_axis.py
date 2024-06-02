import numpy as np


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
