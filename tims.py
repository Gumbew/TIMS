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


def print_w_hist(data):
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


def print_emp_hist(data):
    l = len(data)
    plt.title('Histogram')
    plt.hist(
        range(l),
        bins=l,
        weights=data,
        color="black",
        histtype='step'
    )

    plt.ylabel('n')
    plt.xlabel('x')
    plt.show()


def print_freq_plot(keys, data):
    plt.title('Plot')
    plt.scatter(
        keys,
        data
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


def calc_emp_disc(data):
    emp_table = [0.0]
    for i in range(100):
        emp_table.append(emp_table[-1] + data[i])
    return emp_table


def get_r(n):
    i = 0
    while not (pow(2, i) < n and (n <= pow(2, i + 1))):
        i += 1
    return i


def get_m(i, r, data):
    res = 0
    for item in data:
        if (r + 1) * (i - 1) < item <= (r + 1) * i:
            res += 1
    return res


def get_x_emp(r, n, f, data):
    res = 0
    for i in range(1, r + 1):
        res += (pow((get_m(i, r, data) - n * get_p(r)), 2)) / n * get_p(r)
    return res


def get_p(r):
    return 1 / (r + 1)


def main():
    data_file = "heh.data"
    top = 100
    amount = 1000
    gen_data(data_file, amount, top)
    data = read_data(data_file)

    data = np.sort(np.array(data))

    freq_table = calc_frequency(data)

    w_arr = calc_w(freq_table, amount)

    print_w_hist(w_arr)

    emp_table = calc_emp_disc(w_arr)
    print_emp_hist(emp_table)

    # print_freq_plot(freq_table.keys(),freq_table.values())


main()
