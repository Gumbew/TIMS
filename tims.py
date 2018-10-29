import collections
import os.path
import random
from scipy import stats

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
    while (not (pow(2, i) < n and (n <= pow(2, i + 1)))):
        i += 1
    return i


def get_m(i, r, data):
    res = 0
    for item in data:
        if ((r + 1) * (i - 1) < item and item <= (r + 1) * i):
            res += 1
    return res


def get_x_emp(r, n, f, data):
    res = 0
    for i in range(1, r + 1):
        res += (pow((get_m(i, r, data) - n * get_p(r)), 2)) / n * get_p(r)
    return res


def get_p(r):
    return 1 / (r + 1)


def make_cont_table(data,amount):
    step =get_r(amount)+1
    res = []
    i = 0
    while(i<len(data)):
        res.append(data[i:i+step])
        i+=step
    return res

def make_count_avg_values(data):
    res=[]
    for i in data:
        res.append(np.mean(i))
    return res

def numerical_characteristics(data):
    data=np.array(data)
    mode = stats.mode(data)
    print('Мода: ', int(mode[0]))
    mean = data.mean()
    print('Середнє значення: ', mean)
    median = np.median(data)
    print('Медіана: ', median)
    variansa = data.var()
    print('Варіанса', variansa)
    range = data.max() - data.min()
    print('Розмах: ', range)
    variatsiya = (variansa ** 0.5) / mean
    print('Варіація: ', variatsiya)
    quantil = np.quantile(data,q=[0.25, 0.5, 0.75])
    de = np.quantile(data,q=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    IDR = de[8] - de[0]
    print('Інтердецильна широта', IDR)
    IQR = quantil[2] - quantil[0]
    print('Інтерквантильна широта', IQR)
    asm = stats.skew(data)
    print('Асиметрія: ', asm)
    eks = stats.kurtosis(data)
    print('Ексцес', eks)



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

    arr =make_cont_table(data,amount)
    arr=np.array(arr)
    #print(arr)
    res = make_count_avg_values(arr)
    #print(res)
    print("Дистретні \n")
    numerical_characteristics(data)
    print()
    print("Неперервні \n")
    numerical_characteristics(res)

main()
