import numpy as np
import matplotlib.pyplot as plt


def object_rotation(obj, deg):
    deg_radians = np.radians(deg)

    # матриця повороту
    rotation_matrix = np.array([
        [np.cos(deg_radians), -np.sin(deg_radians)],
        [np.sin(deg_radians), np.cos(deg_radians)]
    ])

    rotated_obj = np.dot(obj, rotation_matrix)

    return rotated_obj

