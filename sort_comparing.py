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
    print(f'Array faster than list by {res_ar - res_l} seconds. {res_ar / res_l} times more.')
    return res_l, res_ar


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


def sort_with_merge(seq):
    bgn = perf_counter()
    #print(seq)
    if type(seq) == list:
        sub_seqs = [True]
        sub_seqs[0] = [seq.pop(0), ]
        for i in range(len(seq)):
            for j in range(len(sub_seqs)):
                if seq[i] > sub_seqs[j][-1]:
                    sub_seqs[j].append(seq[i])
                    break
            else:
                sub_seqs.append([seq[i],])
        seq.clear()
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
            seq.append(sub_seqs[smallest_i].pop(0))
            for i in range(len(i_empty)-1, -1, -1):
                del sub_seqs[i_empty[i]]
    else:
        sub_seqs = [np.array([seq[0], ]), ]
        seq = seq[1:]
        for i in range(len(seq)):
            for j in range(len(sub_seqs)):
                if seq[i] > sub_seqs[j][-1]:
                    sub_seqs[j] = np.append(sub_seqs[j], seq[i])
                    break
            else:
                new = np.array([seq[i], ])
                sub_seqs.append(new)
        seq = np.array([])
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
            seq = np.append(seq, sub_seqs[smallest_i][0])
            sub_seqs[smallest_i] = np.delete(sub_seqs[smallest_i], 0)
            for i in range(len(i_empty) - 1, -1, -1):
                del sub_seqs[i_empty[i]]
    end = perf_counter()
    seq = np.hstack([seq, sub_seqs[0]])
    print(seq, '\n', f'For {type(seq)} it is lasted for {end-bgn} seconds')
    return end - bgn


def quick_sort(seq):
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
    if type(seq) == list:
        seq = inner_sort_list(seq)
    else:
        seq = inner_sort_ar(seq)
    end = perf_counter()
    print(seq, '\n', f'For {type(seq)} it is lasted for {end - bgn} seconds')
    return end - bgn


# row, row_ar = row_making(500)
# print(row)
# quick_sort(row)
# compare_types(sort_with_merge(row), sort_with_merge(row_ar))
# print(compare_sorts(row_ar, py_sort, bubble_sort, sort_with_select_man, sort_with_insert, sort_with_merge, quick_sort))


# row, row_ar = row_making(1000)
# print(row)
# sort_with_merge(row)
# compare_types(sort_with_merge(row), sort_with_merge(row_ar))
# print(compare_sorts(row_ar, py_sort, bubble_sort, sort_with_select_man, sort_with_insert, sort_with_merge))
# describe_row(row)

