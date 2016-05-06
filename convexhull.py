from collections.abc import Sequence

"""
   Convex Hull Assignment: COSC262 (2016)
   Student Name: Radu Fracea
   Usercode: rcf30
"""
class Point():
    def __init__(self, x, y):
        self.point = [x, y]

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
            listPts.append(Point(x,y))
    return listPts

def lineFn(ptA, ptB, ptC):
    return ((ptB[0]-ptA[0])*(ptC[1]-ptA[1]) - (ptB[1]-ptA[1])*(ptC[0]-ptA[0]))

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
    if lineFn(ptA, ptB, ptC) * lineFn(ptA, ptB, ptD) < 0  and lineFn(ptC, ptD, ptA) * lineFn(ptC, ptD, ptB) < 0:
        return True
    else:
        if isPtOnSegment(ptA, ptB, ptC) or isPtOnSegment(ptA, ptB, ptD):
            return True
        else:
            if isPtOnSegment(ptC, ptD, ptA) or isPtOnSegment(ptC, ptD, ptB):
                return True
            else:
                return False


def giftwrap(listPts):
    """Returns the indices of hull vertices computed using giftwrap algorithm
    """
    pass
    #Your implementation goes here
    #return chull


def grahamscan(listPts):
    """Returns the indices of hull vertices computed using grahamscan algorithm
    """
    pass
    #Your implementation goes here
    #return  chull

def amethod(listPts):
    """Returns the indices of hull vertices computed using a third algorithm
    """
    pass
    #Your implementation goes here
    #return chull

def main():
    listPts = readDataPts('Data/A_10.dat')  #File name given as example only
    #print(giftwrap(listPts))      #You may replace these three print statements
    #print (grahamscan(listPts))   #with any code for validating your outputs
    #print (amethod(listPts))      #using the data provided in .out files
    print(listPts)


if __name__  ==  "__main__":
    main()
