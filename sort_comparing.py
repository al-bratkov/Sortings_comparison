import copy
import numpy as np
import random as rd
from time import perf_counter


def row_making(length):
    row = list(range(length))
    rd.shuffle(row)
    row_ar = np.array(row)
    return row, row_ar


def describe_row(seq):
    seq = np.array(seq)
    ordered_seq = sorted(seq)
    residual = seq - ordered_seq
    # print(f'The median of this sequence is {np.median(residual)} and the standart deviation is {np.std(residual)}')
    return np.median(residual), np.std(residual)


def compare_types(func, size):
    seq, seq_ar = row_making(size)
    res_l = func(seq)
    res_ar = func(seq_ar)
    print(f'Array is faster than list by {res_l - res_ar} seconds. {res_l / res_ar} times more.')
    return res_l, res_ar


def compare_sorts(seq, *funcs):
    pass
    res = []
    for func in funcs:
        res.append(func(seq))
    return res


def py_sort(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    inner_seq = sorted(inner_seq)
    end = perf_counter()
    return end - bgn


def bubble_sort(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    flag_fin = False
    circle = 1
    # print(seq)
    while flag_fin == False:
        flag_fin = True
        for i in range(len(inner_seq) - circle):
            if inner_seq[i] > inner_seq[i + 1]:
                flag_fin = False
                inner_seq[i], inner_seq[i + 1] = inner_seq[i + 1], inner_seq[i]
        circle += 1
    end = perf_counter()
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_select_man(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    # print(seq)
    if type(inner_seq) == list:
        for i in range(len(inner_seq)):
            smallest = inner_seq[0]
            smallest_i = 0
            for j in range(len(inner_seq) - i):
                if inner_seq[j] < smallest:
                    smallest = inner_seq[j]
                    smallest_i = j
            inner_seq.append(smallest)
            del inner_seq[smallest_i]
    else:
        for i in range(len(inner_seq)):
            smallest = inner_seq[0]
            smallest_i = 0
            for j in range(len(inner_seq) - i):
                if inner_seq[j] < smallest:
                    smallest = inner_seq[j]
                    smallest_i = j
            inner_seq = np.append(inner_seq, smallest)
            inner_seq = np.delete(inner_seq, smallest_i)
    end = perf_counter()
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_select_prog(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    l = len(inner_seq)
    # print(seq)
    if type(inner_seq) == list:
        for i in range(len(inner_seq)):
            smallest = min(inner_seq[:l - i])
            smallest_i = inner_seq.index(smallest)
            inner_seq.append(smallest)
            del inner_seq[smallest_i]
    else:
        for i in range(len(inner_seq)):
            smallest = min(inner_seq[:l - i])
            smallest_i = np.where(inner_seq == smallest)
            inner_seq = np.append(inner_seq, smallest)
            inner_seq = np.delete(inner_seq, smallest_i)
    end = perf_counter()
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_insert(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    # print(seq)
    if type(inner_seq) == list:
        for i in range(1, len(inner_seq)):
            j = 0
            while (inner_seq[i] > inner_seq[j]) and (j < i):
                j += 1
            inner_seq.insert(j, inner_seq.pop(i))
    else:
        for i in range(1, len(inner_seq)):
            j = 0
            while (inner_seq[i] > inner_seq[j]) and (j < i):
                j += 1
            x = inner_seq[i]
            inner_seq = np.insert(inner_seq, j, x)
            inner_seq = np.delete(inner_seq, i + 1)
    end = perf_counter()
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def sort_with_merge(seq):
    inner_seq = copy.copy(seq)
    bgn = perf_counter()
    #print(seq)
    if type(inner_seq) == list:
        sub_seqs = [True]
        sub_seqs[0] = [inner_seq.pop(0), ]
        for i in range(len(inner_seq)):
            for j in range(len(sub_seqs)):
                if inner_seq[i] > sub_seqs[j][-1]:
                    sub_seqs[j].append(inner_seq[i])
                    break
            else:
                sub_seqs.append([inner_seq[i], ])
        inner_seq.clear()
        while len(sub_seqs) > 1:
            i_empty = []
            smallest = sub_seqs[0][0]
            smallest_i = 0
            for i in range(len(sub_seqs)):
                try:
                    if sub_seqs[i][0] < smallest:
                        smallest = sub_seqs[i][0]
                        smallest_i = i
                except IndexError:
                    i_empty.append(i)
            inner_seq.append(sub_seqs[smallest_i].pop(0))
            for i in range(len(i_empty)-1, -1, -1):
                del sub_seqs[i_empty[i]]
    else:
        sub_seqs = [np.array([inner_seq[0], ]), ]
        inner_seq = inner_seq[1:]
        for i in range(len(inner_seq)):
            for j in range(len(sub_seqs)):
                if inner_seq[i] > sub_seqs[j][-1]:
                    sub_seqs[j] = np.append(sub_seqs[j], inner_seq[i])
                    break
            else:
                new = np.array([inner_seq[i], ])
                sub_seqs.append(new)
        inner_seq = np.array([])
        while len(sub_seqs) > 1:
            i_empty = []
            smallest = sub_seqs[0][0]
            smallest_i = 0
            for i in range(len(sub_seqs)):
                try:
                    if sub_seqs[i][0] < smallest:
                        smallest = sub_seqs[i][0]
                        smallest_i = i
                except IndexError:
                    i_empty.append(i)
            inner_seq = np.append(inner_seq, sub_seqs[smallest_i][0])
            sub_seqs[smallest_i] = np.delete(sub_seqs[smallest_i], 0)
            for i in range(len(i_empty) - 1, -1, -1):
                del sub_seqs[i_empty[i]]
    end = perf_counter()
    type_of = type(inner_seq)
    inner_seq = np.hstack([inner_seq, sub_seqs[0]])
    if type_of == list:
        inner_seq = list(inner_seq)
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


def quick_sort(seq):
    inner_seq = copy.copy(seq)
    # print(seq)
    def inner_sort_list(in_seq):
        if len(in_seq) < 2:
            return in_seq
        pivot = in_seq[-1]
        pos = 0
        for i in range(len(in_seq) - 2, -1, -1):
            if in_seq[i] > pivot:
                in_seq.append(in_seq.pop(i))
            else:
                pos += 1
        less_half = in_seq[:pos]
        more_half = in_seq[pos + 1:]
        less_half = inner_sort_list(less_half)
        more_half = inner_sort_list(more_half)
        in_seq = less_half + [pivot, ] + more_half
        return in_seq

    def inner_sort_ar(in_seq):
        if len(in_seq) < 2:
            return in_seq
        pivot = in_seq[-1]
        pos = 0
        for i in range(len(in_seq) - 2, -1, -1):
            if in_seq[i] > pivot:
                in_seq = np.append(in_seq, in_seq[i])
                in_seq = np.delete(in_seq, i)
            else:
                pos += 1
        less_half = in_seq[:pos]
        more_half = in_seq[pos + 1:]
        less_half = inner_sort_ar(less_half)
        more_half = inner_sort_ar(more_half)
        less_half = np.append(less_half, pivot)
        in_seq = np.hstack([less_half, more_half])
        return in_seq

    bgn = perf_counter()
    if type(inner_seq) == list:
        inner_seq = inner_sort_list(inner_seq)
    else:
        inner_seq = inner_sort_ar(inner_seq)
    end = perf_counter()
    print(inner_seq, '\n', f'For {type(inner_seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


# row, row_ar = row_making(100)
# print(row)
# py_sort(row)
# print(min(compare_types(bubble_sort, 100)))
# print(compare_sorts(row_ar, py_sort, bubble_sort, sort_with_select_man, sort_with_insert, sort_with_merge, quick_sort))


# row, row_ar = row_making(1000)
# print(row)
# sort_with_merge(row)
# compare_types(sort_with_merge(row), sort_with_merge(row_ar))
# print(compare_sorts(row_ar, py_sort, bubble_sort, sort_with_select_man, sort_with_insert, sort_with_merge))
# describe_row(row)

# https://towardsdatascience.com/python-lists-are-sometimes-much-faster-than-numpy-heres-a-proof-4b3dad4653ad
#
