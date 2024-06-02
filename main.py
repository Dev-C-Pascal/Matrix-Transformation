import numpy as np
import plot_drawing
from matrix_transformation import object_rotation_by_angle

Batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
    [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]
])

Object = np.array([
    [1, 1], [0, 0], [1, 0], [3, 4], [4, 0], [0, 3]
])
plot_drawing.draw_plot(object_rotation_by_angle.object_rotation(Object, 90))
# plot_drawing.draw_plot(Batman, Object)

