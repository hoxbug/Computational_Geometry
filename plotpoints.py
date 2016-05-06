import matplotlib.pyplot as plt
from convexhull import Point, readDataPts, isPtOnSegment, segmentIntn

def plot_points(listPts, plane, color = 'red', size = 4):
    """Plots a given list of (x, y) values on a given figure"""
    x = []
    y = []
    for points in listPts:
        x.append(points[0])
        y.append(points[1])

    plane.scatter(x, y, s = size, c = color, edgecolors = color)

def draw_line(plot_list, plane, color = 'blue'):
    for ptA, ptB in plot_list:
        plane.plot([ptA[0], ptB[0]], [ptA[1], ptB[1]], c = color)

def main():
    """Main function"""
    #listPts = readDataPts('Data/A_10.dat')
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


if __name__ == "__main__":
    main()
