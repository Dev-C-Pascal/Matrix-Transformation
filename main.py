import numpy as np
import plot_drawing
from matrix_transformations import object_rotation_by_angle
from matrix_transformations import scaling_on_coefficient
from matrix_transformations import reflection_by_axis
from matrix_transformations import axis_slope

Batman = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
    [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]
])

Object = np.array([
    [1, 1], [0, 0], [1, 0], [3, 4], [4, 0], [0, 3]
])


# draw to matrix
# plot_drawing.draw_plot(Batman, Object)


# draw one changed matrix
# plot_drawing.draw_plot(object_rotation_by_angle.rotation(Object, 90))


# draw scaled matrix
# plot_drawing.draw_plot(scaling_on_coefficient.scale(Batman, 2))


# draw reflected by axis
# plot_drawing.draw_plot(Object)
# plot_drawing.draw_plot(reflection_by_axis.axis_reflection(Object, 'x'))
# plot_drawing.draw_plot(reflection_by_axis.axis_reflection(Object, 'y'))


# draw sloped by axis
# plot_drawing.draw_plot(axis_slope.slope(Batman, 'y', 5))


def main(custom_matrix):
    choice = input(
        "Axis_slope -> 'a'\n"
        "Object_rotation - > 'o'\n"
        "Reflection_by_axis -> 'r'\n"
        "Scaling_on_coefficient -> 's'\n"
        "Input command that you choose:")
    if choice not in ('a', 'o', 'r', 's'):
        print("You entered wrong number")
    elif choice == 'a':
        plot_drawing.draw_plot(axis_slope.slope(custom_matrix, 'y', 5))
    elif choice == 'o':
        plot_drawing.draw_plot(object_rotation_by_angle.rotation(Object, 90))
    elif choice == 'r':
        plot_drawing.draw_plot(reflection_by_axis.axis_reflection(Object, 'x'))
    elif choice == 's':
        plot_drawing.draw_plot(scaling_on_coefficient.scale(Batman, 2))


if __name__ == '__main__':
    main(Object)
