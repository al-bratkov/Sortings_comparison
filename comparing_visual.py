import pandas as pd

import sort_comparing as sc
import comparing_research as cr
import matplotlib.pyplot as plt
import numpy as np


def select_sort_type():
    flag = False

    while not flag:
        try:
            sort_type = int(input('Select one of these sort types: 1: bubble sort, 2: selection sort, '
                                  '3: insertion sort, 4: merge sort, 5: quick sort'))
            flag = True
        except ValueError:
            print('you entered not a number')
            flag = False
    return sort_type


def compare_type_vis(func, size=100):
    sizes = [10, 100, 200, 500, 750, 1000]
    res = [[], []]
    for s in sizes:
        l, ar = sc.compare_types(func, s)
        res[0].append(l)
        res[1].append(ar)
    plt.plot(sizes, res[0])
    plt.plot(sizes, res[1])
    plt.show()


def compare_sorts_vis(*sort_funcs, sizes=[10, 100, 200, 500, 750, 1000]):
    measuring = {size: 0 for size in sizes}
    row = sc.row_making(1000)[0]
    names = []
    plt.title("Comparing of sorts")
    plt.xlabel("Size of sequence")
    plt.ylabel("Time for sorting (seconds)")
    for func in sort_funcs:
        for size in sizes:
            measuring[size] = func(row[:size])
        plt.scatter(sizes, measuring.values())
        names.append(func.__name__)
    plt.legend(names)
    plt.show()


def compare_size_vis(sort_func, repeats=100, sizes=[10, 100, 200, 500, 750, 1000]):
    measuring = {size: 0 for size in sizes}
    # measuring = {10: 0, 100: 0, 200: 0, 500: 0, 750: 0, 1000: 0}
    for num in measuring.keys():
        for i in range(repeats):
            row = sc.row_making(num)[0]
            measuring[num] += sort_func(row)
    for size, time in measuring.items():
        measuring[size] = time / repeats
    length = tuple(measuring.keys())
    result = tuple(measuring.values())
    return length, result


class VisualiseDatabaseFeatures:
    def __init__(self, df):
        self.df = df

    def vis_dif_types(self, length=0, sort_type_col=""):
        inner_df = self.df[self.df["Length"] == length]
        types = set(self.df["Type"])
        for t in types:
            one_type = inner_df[inner_df["Type"] == t][sort_type_col]
            plt.boxplot(one_type)
            plt.legend(t)
        plt.show()
        # quartiles = np.quantile(inner_df.groupby("Type")[sort_type_col], np.linspace(0, 1, 5))


# compare_sorts_vis(sc.py_sort, sc.bubble_sort, sc.sort_with_select_man, sc.sort_with_insert, sc.sort_with_merge, sc.quick_sort)
test = VisualiseDatabaseFeatures(pd.read_csv("sort.csv"))
test.vis_dif_types(100, "Time quick")
