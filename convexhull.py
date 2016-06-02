
"""
   Convex Hull Assignment: COSC262 (2016)
   Student Name: Radu Fracea
   Usercode: rcf30
"""


class Point:
    """A simple class for the points, takes a x and y value
    """

    def __init__(self, x, y):
        self.point = [int(x), int(y)]

    def __repr__(self):
        return str(tuple(self.point))

    def __getitem__(self, key):
        return self.point[key]


def readDataPts(filename):
    """Reads data from an input file and returns a list of tuples
       [(x0,y0), (x1, y1), ...]
    """
    listPts = []

    with open(filename, 'r') as data:
        num_points = int(data.readline())
        for i in range(num_points):
            point = tuple(data.readline().strip().split())
            x, y = point
            listPts.append(Point(x, y))
    return listPts


def lineFn(ptA, ptB, ptC):
    return ((ptB[0] - ptA[0]) * (ptC[1] - ptA[1]) - (ptB[1] - ptA[1]) *
            (ptC[0] - ptA[0]))


def isCCW(ptA, ptB, ptC):
    return lineFn(ptA, ptB, ptC) > 0


def isPtOnSegment(ptA, ptB, ptC):
    lineFn_num = lineFn(ptA, ptB, ptC)
    if abs(lineFn_num) < 1.e-6:
        if (min(ptA[0], ptB[0])) <= ptC[0] <= (max(ptA[0], ptB[0])):
            if (min(ptA[1], ptB[1])) <= ptC[1] <= (max(ptA[1], ptB[1])):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def segmentIntn(ptA, ptB, ptC, ptD):
    if (lineFn(ptA, ptB, ptC) * lineFn(ptA, ptB, ptD) < 0) and  \
       lineFn(ptC, ptD, ptA) * lineFn(ptC, ptD, ptB) < 0:
        return True
    else:
        if isPtOnSegment(ptA, ptB, ptC) or isPtOnSegment(ptA, ptB, ptD):
            return True
        else:
            if isPtOnSegment(ptC, ptD, ptA) or isPtOnSegment(ptC, ptD, ptB):
                return True
            else:
                return False


def theta(ptA, ptB):
    ''' Computes an approximation of the angle between the line AB and a
        horizontal line through A.
    '''
    dx = ptB[0] - ptA[0]
    dy = ptB[1] - ptA[1]

    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        t = 0
    else:
        t = dy / (abs(dx) + abs(dy))

    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t

    return t * 90


def getBottomRight(listPts):
    """Returns the index of the  bottom right most point, used in the start of some of
       the algorithms
    """
    points = sorted(listPts, key=lambda x: (x.point[1], -x.point[0]))

    return listPts.index(points[0])


def simpleClosedPath(listPts):
    """Returns the closed path of the given points"""

    points = listPts[:]  # making a compy of the listPts
    y_min_index = getBottomRight(listPts)
    y_min_point = points.pop(y_min_index)

    closed_path = [(y_min_point, 0)]

    for point in points:
        angle = theta(y_min_point, point)

        closed_path.append((point, angle))

    closed_path.sort(key=lambda x: x[1])

    return [x[0] for x in closed_path]


def convexHullIndex(convex_hull, listPts):
    """Returns the indices of of the given points of the convex_hull from the listPts
    """
    output = []

    for point in convex_hull:
        output.append(listPts.index(point))

    return output

# !!!!
# Should be done, just have a look over again when your done
# !!!!


def giftwrap(listPts):
    """Returns the indices of hull vertices computed using giftwrap algorithm
    """
    points_list = listPts[:]  # copy of the points list which we manipulate
    convex_hull = []  # list of the points on the convex hull

    k = getBottomRight(points_list)

    i = 0
    v = 0
    n = len(points_list)

    points_list.append(listPts[k])
    convex_hull.append(points_list[k])

    run = True

    while run:
        # Swap Pi and Pk
        points_list[i], points_list[k] = points_list[k], points_list[i]

        minAngle = 361

        # compute angle of line point i and the points that are not part
        # of the convex hull yet
        for j in range(i + 1, n + 1):
            angle = theta(points_list[i], points_list[j])

            if angle == 0:
                # for Ambiguous case where 0 degrees is 360 degrees
                angle = 360

            if (angle < minAngle and angle > v and points_list[j] != points_list[i]):
                minAngle = angle
                k = j

        v = minAngle
        i = i + 1

        if points_list[0] != points_list[k]:
            # Breaks if the next point of the convex hull is the start of the
            # convex hull, meaning we have completed the convex hull.
            convex_hull.append(points_list[k])
        else:
            run = False

    output = convexHullIndex(convex_hull, listPts)

    return output

# !!!!
# Finished, should not need any more work.
# !!!!


def grahamscan(listPts):
    """Returns the indices of hull vertices computed using grahamscan algorithm
    """

    closed_loop = simpleClosedPath(listPts)  # points of the closed loop

    # putting first 3 points from the closed_loop on the stack
    stack = closed_loop[0:3]
    closed_loop = closed_loop[2:]  # closed_loop without the first 3 points

    # while there are points in the closed_loop
    while len(closed_loop) > 0:
        if isCCW(stack[-2], stack[-1], closed_loop[0]):
            # if point 3 isCCW of the line from point1 - point2, append point
            # on stack
            stack.append(closed_loop[0])
            closed_loop.pop(0)
        else:
            # else remove point 3 from top of stack
            stack.pop()

    output = convexHullIndex(stack, listPts)

    return output

# !!!!
# Implement own method
# !!!!


def amethod(listPts):
    """Returns the indices of hull vertices computed using a third algorithm
    """
    # sorting  the points min  y-cord and max x-cord
    points = sorted(listPts, key=lambda x: (x.point[1], -x.point[0]))

    right = []  # the right side of the convex haul
    left = []  # the left side of the convex haul

    # makes the right side of the convex haul
    for point in points:
        while len(right) >= 2 and not isCCW(right[-2], right[-1], point):
            right.pop()
        right.append(point)

    # makes the left side of the convex haul
    for point in reversed(points):
        while len(left) >= 2 and not isCCW(left[-2], left[-1], point):
            left.pop()
        left.append(point)

    convex_haul = right

    # Could have skipped this and just returned set of right + left
    # But wanted to get the convex haul in a counter clock wise rotation
    for point in left:
        if point not in convex_haul:
            convex_haul.append(point)

    output = convexHullIndex(convex_haul, listPts)

    return output
    # Your implementation goes here
    # return chull


def test_data(convex_hull, answer):
    for i in range(len(answer)):
        if convex_hull[i] == answer[i]:
            print("|Correct: {} = {}".format(convex_hull[i], answer[i]))
        else:
            print("/Incorrect: {} != {}".format(convex_hull[i], answer[i]))


def read_answer(filename):
    import shlex
    listPts = []

    with open(filename, 'r') as data:
        answers = data.readline()
        answers = ",".join(shlex.split(answers))
        answers = answers.split(",")
        for i in answers:
            listPts.append(int(i))

    return listPts


def main():
    testFile = "B_30000"
    # File name given as example only
    print("-" * 80)
    listPts = readDataPts('Data/{}.dat'.format(testFile))
    answers = read_answer('Data/{}.out'.format(testFile))
    # convex_hull = grahamscan(listPts)
    # convex_hull = giftwrap(listPts)
    convex_hull = amethod(listPts)
    test_data(convex_hull, answers)
    # print(convex_hull)
    # for i in convex_hull:
    #    print("Index: {}, Point: {}".format(i, listPts[i]))

    # print()
    # print("Index: 4, Point: {}".format(listPts[4]))
    # print("Index: 8, Point: {}".format(listPts[8]))
    # print("Index: 1, Point: {}".format(listPts[1]))

    # You may replace these three print statements
    # print (grahamscan(listPts))   #with any code for validating your outputs
    # print (amethod(listPts))      #using the data provided in .out files
    # print(listPts)


if __name__ == "__main__":
    main()
