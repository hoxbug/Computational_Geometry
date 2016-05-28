import matplotlib.pyplot as plt
from convexhull import Point
from plotpoints import plot_points, draw_line

def example_plot_points():
    """Basic example of plotting 4 points"""

    # Create a figure and put a plane on the figure
    fig = plt.figure()
    plane = fig.add_subplot(1, 1, 1)

    # Define Points
    A = Point(5, 5)
    B = Point(10, 10)
    C = Point(9, 9)
    D = Point(9, 13)

    list_points = [A, B, C, D]

    plot_points(list_points, plane)

    plt.show()

def example_plot_line_point():
    fig = plt.figure()
    plane = fig.add_subplot(1, 1, 1)

    A = Point(5, 5)
    B = Point(10, 10)
    C = Point(9, 9)
    D = Point(9, 13)
    E = Point(4, 7)
    F = Point(9, 7)
    G = Point(1, 1)
    H = Point(4, 4)
    I = Point(10, 5)
    J = Point(15, 10)

    listPts = [A, B, C, D, E, F, G, H, J]
    listLines = [(A, B), (C, D), (E, F), (G, H), (I, J)]

    plot_points(listPts, plane)
    draw_line(listLines, plane)

    draw_line([], fig)
    plt.show()

def main():
    #example_plot_points()
    example_plot_line_point()

if __name__ == "__main__":
    main()
