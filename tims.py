import collections
import os.path
import random

import matplotlib.pyplot as plt
import numpy as np


def gen_data(file_name, amount, top):
    if os.path.isfile(file_name):
        return
    _data = [random.randrange(0, top) for i in range(amount)]
    f = open(file_name, '+w')
    for element in _data:
        f.write("%s\n" % element)


def read_data(file_name):
    _data = []
    f = open(file_name)
    for element in f.readlines():
        _data.append(int(element))
    return _data


def print_hist(data):
    data_len = len(data)
    plt.title('Histogram')
    plt.hist(
        range(data_len),
        bins=data_len,
        weights=data
    )
    plt.ylabel('n')
    plt.xlabel('x')
    plt.show()


def calc_w(freq_table, amount):
    w_arr = []
    for key, value in freq_table.items():
        w_arr.append(freq_table[key] / amount)
    return w_arr


def calc_frequency(data):
    return collections.Counter(data)


def main():
    data_file = "heh.data"
    top = 100
    amount = 1000
    gen_data(data_file, amount, top)
    data = read_data(data_file)

    data = np.sort(np.array(data))

    freq_table = calc_frequency(data)

    w_arr = calc_w(freq_table, amount)

    print_hist(w_arr)


main()
