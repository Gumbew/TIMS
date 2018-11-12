import collections
import math
import os.path
import random

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

top = 5
amount = 20

# генеруємо вибірку
def gen_data(file_name):
    if os.path.isfile(file_name):
        return
    _data = [random.randrange(0, top) for i in range(amount)]
    f = open(file_name, '+w')
    for element in _data:
        f.write("%s\n" % element)


# зчитуємо дані в масив
def read_data(file_name):
    _data = []
    f = open(file_name)
    for element in f.readlines():
        _data.append(int(element))
    return _data


def read_cont_data(file_name):
    _data = []
    f = open(file_name)
    for element in f.readlines():
        _data.append(float(element))
    return _data


def read_freq_data(file_name):
    _data = {}
    f = open(file_name)
    for element in f.readlines():
        _data[int(element.split(':')[0])] = int(element.split(':')[1])
    _data = collections.OrderedDict(sorted(_data.items()))
    _data = dict(_data)
    return _data


def make_var_row(data):
    res = []
    for item in data:
        for i in range(data[item]):
            res.append(item)
    return res


# варіаційний ряд для неперервних
def print_w_hist(data, w, data_c):
    step = (max(data_c) - min(data_c)) / (get_r(len(data_c)) + 1)
    n = 0
    for i in w:
        n += i

    plt.subplot(2, 3, 1)
    plt.title('Діаграма частот')

    plt.hist(
        data,
        weights=w / n,
        edgecolor="black",
        color="Red",
        bins=np.arange(min(data_c), max(data_c) + step, step)
    )
    plt.ylabel('w')
    plt.xlabel('x')
    plt.xticks(data)


# статистичний розподіл для неперервних
def print_n_hist(data, w, data_c):
    step = (max(data_c) - min(data_c)) / (get_r(len(data_c)) + 1)
    plt.subplot(2, 3, 2)
    plt.title('Діаграма частот')
    plt.hist(
        data,
        weights=w,
        bins=np.arange(min(data_c), max(data_c) + step, step),
        edgecolor='black',
        align='mid',
        color="Red"
    )

    plt.xticks(data)
    plt.xlabel('x')
    plt.ylabel('n')


# Варіаційний ряд для дискретної величини
def print_w_plot(data):
    plt.subplot(2, 3, 4)
    data_len = len(data)
    plt.title('Полігон частот')
    plt.scatter(
        range(data_len),
        data
    )
    plt.plot(range(data_len), data, '-y')
    plt.ylabel('w')
    plt.xlabel('x')


# Емпірична функція розподілу
def print_emp_hist(data):
    plt.subplot(2, 3, 6)
    plt.title('Емпірична функція розподілу \n для дискретної статистичної змінної')
    s = {}

    for i in range(-1, top):
        s[data[i + 1]] = [(i, i + 1)]

    for y in s:
        for seg in s[y]:
            plt.plot(seg, [y, y], color='black')


# статистичний розподіл для дискретних
def print_freq_plot(keys, data):
    plt.subplot(2, 3, 5)
    plt.title('Гістограма частот')
    plt.hist(
        range(top),
        bins=np.arange(top + 1) - 0.5,
        weights=data,
        edgecolor="black"

    )
    plt.ylabel('n')
    plt.xlabel('x')
    plt.xticks(keys)


def print_emp_func_cont(emp_values, data_c, data):
    step = (max(data_c) - min(data_c)) / (get_r(len(data_c)) + 1)
    res = []
    for i in range(get_r(len(data_c)) + 1):
        res.append((data[0] + i + 1) * step)
    plt.subplot(2, 3, 3)
    plt.title('Емпірична функція розподілу \n для неперервної статистичної змінної')
    plt.hist(
        data,
        bins=data + [res[-1]],
        weights=emp_values[1:],
        color="black",
        histtype='step',
        edgecolor="black",
        align='left'
    )
    plt.ylabel('n')
    plt.xlabel('x')


# рахує частотні ймовірності для дискретних
def calc_w_disc(freq_table):
    w_arr = []
    for key, value in freq_table.items():
        w_arr.append(freq_table[key] / amount)
    return w_arr


# рахує частотні ймовірності для неперевних
def calc_w_cont(data):
    res = []
    n = 0
    for i in data:
        n += i
    for i in data:
        res.append(i / n)
    return res


# рахує кількість попадань для неперевних
def calc_n_cont(freq_table):
    res = []
    for i in range(get_r(amount) + 1):
        c = 0
        for j in range(get_r(amount) + 1):
            c += freq_table[i * get_r(amount) + 1 + j]
        res.append(c)
    return res


# повертає dictionary з x і кількості їх появи
def calc_frequency(data):
    return collections.Counter(data)


def calc_emp_disc(data):
    emp_table = [0.0]
    for i in range(top):
        emp_table.append(emp_table[-1] + data[i])
    return emp_table


def calc_emp_cont(data):
    emp_table = [0.0]
    for i in range(len(data)):
        emp_table.append(emp_table[-1] + data[i])
    return emp_table


# повертає кількість класів - 1 з вибріки
def get_r(n):
    i = 0
    while not (pow(2, i) < n <= pow(2, i + 1)):
        i += 1
    return i


def get_x_avg(fi, xi):
    res = 0
    for i in range(len(xi)):
        res += fi[i] * xi[i]
    return res


def get_d(xi, x_avg, fi):
    res = 0
    for i in range(top):
        res += (math.pow((xi[i] - x_avg), 2) * fi[i])
    return res


def get_ni(density, xi, a, b):
    res = list()
    res.append((xi[0] - a) * density)
    for i in range(1, len(xi) - 1):
        res.append((xi[i + 1] - xi[i]) * density)
    res.append((b - xi[-1]) * density)
    s = 0
    for i in range(len(res)):
        if res[i] < 0:
            res[i] = 0
        s += res[i]
    if s < 1:
        res[-1] += 1 - s

    return res


def get_x_class():
    res = []
    for i in range(top):
        res.append(i)
    return res


# повертає x емпіричне
def get_x_emp(freq_table):
    res = 0
    fi = calc_w_disc(freq_table)
    xi = get_x_class()
    x_avg = get_x_avg(fi, xi)
    gamma = get_d(xi, x_avg, fi) ** 0.5
    a = x_avg - (3 ** 0.5) * gamma
    b = x_avg + (3 ** 0.5) * gamma
    density = 1 / (b - a)
    pi = get_ni(density, xi, a, b)
    for i in range(top):
        if pi[i] == 0:
            continue
        else:
            res += (math.pow(fi[i] - pi[i], 2) / pi[i])
    return res


# розбиває посортовану вибірку на класи
def make_cont_table(data):
    step = (max(data) - min(data)) / (get_r(len(data)) + 1)
    res = []
    count_arr = []
    for i in range(get_r(len(data)) + 1):
        res.append((data[0] + i + 1) * step)

    for i in range(get_r(len(data)) + 1):
        count = 0
        for j in range(len(data)):
            if data[j] >= data[0] + i * step and (data[j] <= data[0] + step * (i + 1)):
                count += 1
        count_arr.append(count)
    return res, count_arr


# повертає список середніх значень в проміжках
def make_cont_avg_values(data):
    res = []
    step = (max(data) - min(data)) / (get_r(len(data)) + 1)
    for i in range(get_r(len(data)) + 1):
        res.append(((data[0] + i * step) + (data[0] + step * (i + 1))) / 2)
    return res, step


# числові характеристики
def numerical_characteristics(data):
    data = np.array(data)
    mode = stats.mode(data)
    print('Мода: ', mode[0])
    mean = data.mean()
    print('Середнє значення: ', mean)
    median = np.median(data)
    print('Медіана: ', median)
    var = data.var()
    print('Варіанса', var)
    scope = data.max() - data.min()
    print('Розмах: ', scope)
    standard = var ** 0.5
    print('Стандарт: ', standard)
    variation = (var ** 0.5) / mean
    print('Варіація: ', variation)
    quartil = np.quantile(data, q=[0.25, 0.5, 0.75])
    de = np.quantile(data, q=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    idr = de[8] - de[0]
    print('Інтердецильна широта', idr)
    iqr = quartil[2] - quartil[0]
    print('Інтерквантильна широта', iqr)
    asm = stats.skew(data)
    print('Асиметрія: ', asm)
    eks = stats.kurtosis(data)
    print('Ексцес', eks)


def print_plots(w_arr, emp_table, k, v, count_w, emp_table_cont, cont_avg, data_c):
    print_w_plot(w_arr)
    print_w_hist(cont_avg, count_w, data_c)

    print_freq_plot(k, v)
    print_n_hist(cont_avg, count_w, data_c)
    print_emp_hist(emp_table)
    print_emp_func_cont(emp_table_cont, data_c, cont_avg)
    plt.show()


def print_freq_count_table(data):
    arr, count_w = make_cont_table(data)
    cont_avg, step = make_cont_avg_values(data)
    res = {}
    for i in range(len(cont_avg)):
        res['{}-{}'.format(format(cont_avg[i] - step / 2, '.2f'), format(cont_avg[i] + step / 2, '.2f'))] = count_w[i]
    return res


def pirson(emp, crit, freq_table):
    if emp < crit:
        print("Гіпотезу приймаємо")
    else:
        print("Гіпотезу відкидаємо")

    print("Емпіричне: ", get_x_emp(freq_table))
    print("Критичне: ", stats.chi2.isf(0.05, top - 3))


def main():
    data_file = "heh.data"
    gen_data(data_file)
    data = read_data(data_file)
    data_c = read_cont_data('cont.txt')
    data_c = np.sort(np.array(data_c))
    data = np.sort(np.array(data))
    freq_table = calc_frequency(data)
    w_arr = calc_w_disc(freq_table)
    arr, count_w = make_cont_table(data_c)
    count_w = np.array(count_w)
    cont_avg, step = make_cont_avg_values(data_c)
    emp_table = calc_emp_disc(w_arr)
    emp_table_cont = calc_w_cont(count_w)
    emp_table_cont = calc_emp_cont(emp_table_cont)

    print('Варіаційний ряд для дискретної змінної \n', data)
    print('Статистичний розподіл варіанти для дискретної змінної \n', dict(freq_table))
    print('Варіаційний ряд для неперервної змінної \n', data_c)
    print('Статистичний розподіл варіанти для неперервної змінної \n', print_freq_count_table(data_c))

    # fd = read_freq_data('freq_data')
    # print(fd)
    # g = np.array(make_var_row(fd))
    # print(g)
    # print(w_arr)

    print("Дискретні \n")
    numerical_characteristics(data)
    print("Неперервні \n")
    numerical_characteristics(data_c)

    pirson(get_x_emp(freq_table), stats.chi2.isf(0.05, top - 3), freq_table)

    print_plots(w_arr, emp_table, list(freq_table.keys()), list(freq_table.values()), count_w,
                emp_table_cont, cont_avg, data_c)


main()
