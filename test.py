from convexhull import readDataPts, giftwrap, grahamscan, amethod
from time import time

tests_A = [("A_10", 10), ("A_50", 50), ("A_500", 500), ("A_3000", 3000),
           ("A_6000", 6000), ("A_9000", 9000), ("A_15000", 15000), ("A_30000", 30000)]
tests_B = [("B_10", 10), ("B_50", 50), ("B_500", 500), ("B_3000", 3000),
           ("B_6000", 6000), ("B_9000", 9000), ("B_15000", 15000), ("B_30000", 30000)]


def read_answer(filename):
    """ Returns the point from the .out file in the Data folder"""
    import shlex
    listPts = []

    filename = "Data/{}.out".format(filename)

    with open(filename, 'r') as data:
        answers = data.readline()
        answers = ",".join(shlex.split(answers))
        answers = answers.split(",")
        for i in answers:
            listPts.append(int(i))

    return listPts


def test_all_same_answer(tests=tests_A):
    for test_case in tests:
        answer = read_answer(test_case)
        filename = "Data/{}.dat".format(test_case)
        listPts = readDataPts(filename)

        gift = giftwrap(listPts)
        graham = grahamscan(listPts)
        mono_tone = amethod(listPts)

        print("Giftwrap = answer: {}".format(gift == answer))
        print("Grahamscan = answer: {}".format(graham == answer))
        print("Monotone Chain = answer: {}".format(mono_tone == answer))


def benchmark(func, test):

    filename = "Data/{}.dat".format(test)
    listPts = readDataPts(filename)

    times = []

    time1 = time()
    result = func(listPts)
    time2 = time()
    result = func(listPts)
    time3 = time()
    result = func(listPts)
    time4 = time()
    result = func(listPts)
    time5 = time()
    result = func(listPts)
    time6 = time()

    times.append(time2 - time1)
    times.append(time3 - time2)
    times.append(time4 - time3)
    times.append(time5 - time4)
    times.append(time6 - time5)

    total_time = 0

    for i in times:
        total_time += i

    average = total_time / len(times)

    return average


def tests_results(func, test_set):
    point_time = []

    for test, points in test_set:
        result = benchmark(func, test)
        point_time.append((points, result))

    return point_time


def main():
    from csv import writer

    with open("results.csv", "w") as output:
        print("-" * 80)
        write_out = writer(output)
        write_out.writerow(("Data Set A",))
        write_out.writerow(
            ("Points", "Giftwrap", "Grahmscan", "Monotone Chain"))

        times_A_gift = tests_results(giftwrap, tests_A)
        times_A_grahm = tests_results(grahamscan, tests_A)
        times_A_mono = tests_results(amethod, tests_A)

        for i in range(len(times_A_gift)):
            write_out.writerow((times_A_gift[i][0], times_A_gift[i][1],
                                times_A_grahm[i][1], times_A_mono[i][1]))
        print("Data set A done")

        write_out.writerow("")
        write_out.writerow(("Data Set B",))

        print("-" * 80)

        times_B_gift = tests_results(giftwrap, tests_B)
        times_B_grahm = tests_results(grahamscan, tests_A)
        times_B_mono = tests_results(amethod, tests_B)

        for i in range(len(times_B_gift)):
            write_out.writerow((times_B_gift[i][0], times_B_gift[i][
                               1], times_B_grahm[i][1], times_B_mono[i][1]))
        print("Data set B done")


if __name__ == "__main__":
    print()
    main()
