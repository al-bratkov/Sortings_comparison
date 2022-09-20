import numpy as np
import random as rd
from time import perf_counter

row = list(range(1000))
rd.shuffle(row)
row_ar = np.array(row)


def describe_row(seq):
    seq = np.array(seq)
    ordered_seq = sorted(seq)
    residual = seq - ordered_seq
    print(f'The median of this sequence is {np.median(residual)} and the standart deviation is {np.std(residual)}')


def compare_types(func_list, func_arr):
    print(f'Array faster than list by {func_arr - func_list} seconds. {func_arr / func_list} times more.')
    return func_arr - func_list


def compare_sorts(seq, *funcs):
    pass
    res = []
    for func in funcs:
        res.append(func(seq))
    return res


def py_sort(seq):
    bgn = perf_counter()
    seq = sorted(seq)
    end = perf_counter()
    return end - bgn


def bubble_sort(seq):
    bgn = perf_counter()
    flag_fin = False
    circle = 1
    # print(seq)
    while flag_fin == False:
        flag_fin = True
        for i in range(len(seq) - circle):
            if seq[i] > seq[i + 1]:
                flag_fin = False
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        circle += 1
    end = perf_counter()
    print(seq, '\n', f'For {type(seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_select_man(seq):
    bgn = perf_counter()
    # print(seq)
    if type(seq) == list:
        for i in range(len(seq)):
            smallest = seq[0]
            smallest_i = 0
            for j in range(len(seq) - i):
                if seq[j] < smallest:
                    smallest = seq[j]
                    smallest_i = j
            seq.append(smallest)
            del seq[smallest_i]
    else:
        for i in range(len(seq)):
            smallest = seq[0]
            smallest_i = 0
            for j in range(len(seq) - i):
                if seq[j] < smallest:
                    smallest = seq[j]
                    smallest_i = j
            seq = np.append(seq, smallest)
            seq = np.delete(seq, smallest_i)
    end = perf_counter()
    print(seq, '\n', f'For {type(seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_select_prog(seq):
    bgn = perf_counter()
    l = len(seq)
    # print(seq)
    if type(seq) == list:
        for i in range(len(seq)):
            smallest = min(seq[:l - i])
            smallest_i = seq.index(smallest)
            seq.append(smallest)
            del seq[smallest_i]
    else:
        for i in range(len(seq)):
            smallest = min(seq[:l - i])
            smallest_i = np.where(seq == smallest)
            seq = np.append(seq, smallest)
            seq = np.delete(seq, smallest_i)
    end = perf_counter()
    print(seq, '\n', f'For {type(seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_insert(seq):
    bgn = perf_counter()
    # print(seq)
    if type(seq) == list:
        for i in range(1, len(seq)):
            j = 0
            while (seq[i] > seq[j]) and (j < i):
                j += 1
            seq.insert(j, seq.pop(i))
    else:
        for i in range(1, len(seq)):
            j = 0
            while (seq[i] > seq[j]) and (j < i):
                j += 1
            x = seq[i]
            seq = np.insert(seq, j, x)
            seq = np.delete(seq, i + 1)
    end = perf_counter()
    print(seq, '\n', f'For {type(seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


# sort_with_insert(row_ar)
# compare_types(sort_with_insert (row), sort_with_insert (row_ar))
print(compare_sorts(row_ar, py_sort, bubble_sort, sort_with_select_man, sort_with_insert))
describe_row(row)
