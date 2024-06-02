import numpy as np


def object_rotation(obj, deg):
    deg_radians = np.radians(deg)

    # матриця повороту
    rotation_matrix = np.array([
        [np.cos(deg_radians), -np.sin(deg_radians)],
        [np.sin(deg_radians), np.cos(deg_radians)]
    ])

    # множення матриць
    rotated_obj = np.dot(obj, rotation_matrix)

    return rotated_obj
