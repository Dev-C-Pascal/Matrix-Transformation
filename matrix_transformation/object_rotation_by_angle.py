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


# Приклад об'єкта
object1 = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
    [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]
])

rotated_object1 = object_rotation(object1, 45)


