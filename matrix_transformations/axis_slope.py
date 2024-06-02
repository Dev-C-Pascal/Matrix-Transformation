import numpy as np


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
