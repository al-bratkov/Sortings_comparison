import pandas as pd
import numpy as np
import sort_comparing as sc

sort_types_story = pd.DataFrame(columns=['Length', 'Type', 'Median', 'Std',
                                   'Deviation mean', 'Deviation max', 'Deviation median', 'Deviation std',
                                   'Time py', 'Time bubble', 'Time select', 'Time insert', 'Time merge', 'Time Quick'])


def describe(seq):
    res = dict()
    res['Length'] = len(seq)
    res['Type'] = str(type(seq))
    seq = np.array(seq)
    ordered_seq = sorted(seq)
    deviation = seq - ordered_seq
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


def fill_df(part_to_add, seq):
    half1 = describe(seq).values()
    half2 = timing(seq).values()
    new_row = list(half1) + list(half2)
    part_to_add.append(new_row)
    return part_to_add


def expand_df(part, file='sort.csv'):
    df = pd.DataFrame(part)
    df.to_csv(file, mode='a', header=False)



row = sc.row_making(100)[0]
templ = []
test = fill_df(templ, row)
print(test)

#sort_types_story = pd.DataFrame(test, columns=['Length', 'Type', 'Median', 'Std',
#                                   'Deviation mean', 'Deviation max', 'Deviation median', 'Deviation std',
#                                   'Time py', 'Time bubble', 'Time select', 'Time insert', 'Time merge', 'Time Quick'])

expand_df(test)

