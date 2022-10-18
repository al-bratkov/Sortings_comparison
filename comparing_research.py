import pandas as pd
import numpy as np
import sort_comparing as sc

sort_types_story = pd.DataFrame(columns=['Length', 'Median', 'Std',
                                   'Deviation mean', 'Deviation max', 'Deviation median', 'Deviation std',
                                   'Time py', 'Time bubble', 'Time select', 'Time insert', 'Time merge', 'Time Quick'])


def describe(seq):
    seq = np.array(seq)
    ordered_seq = sorted(seq)
    deviation = seq - ordered_seq
    res = dict()
    res['Length'] = len(seq)
    res['Median'] = np.median(seq)
    res['Std'] = np.std(seq)
    res['Deviation mean'] = np.mean(deviation)
    res['Deviation max'] = np.max(deviation)
    res['Deviation median'] = np.median(deviation)
    res['Deviation std'] = np.std(deviation)
    return res


def timing(seq):
    res = dict()
    res['Time py'] = sc.py_sort(seq)
    res['Time bubble'] = sc.bubble_sort(seq)
    res['Time select'] = sc.sort_with_select_man(seq)
    res['Time insert'] = sc.sort_with_insert(seq)
    res['Time merge'] = sc.sort_with_merge(seq)
    res['Time quick'] = sc.quick_sort(seq)
    return res


def fill_row(ar, seq):
    describe_columns = describe(seq).values()
    timing_columns = timing(seq).values()
    new_row = list(describe_columns) + list(timing_columns)
    ar = ar.append(np.array(new_row))
    return ar


def fill_df(df, size):
    ar = np.array

def make_stat(n):
    pass


row = sc.row_making(100)[0]
print(fill_row(row))
