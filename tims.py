import collections
import os.path
import random
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np


# генеруємо вибірку
def gen_data(file_name, amount, top):
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


# варіаційний ряд для неперервних
def print_w_hist(data):
    #data_len = len(data)
    plt.title('Task 1 cont')
    data_mod = []
    for i in data:
        for j in range(10):
            data_mod.append(i / 10)
    plt.hist(
        range(len(data_mod)),
        rwidth=10,
        weights=data_mod,
        edgecolor="black"
    )
    plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
    plt.ylabel('w')
    plt.xlabel('x')
    plt.show()


#статистичний розподіл для неперервних
def print_n_hist(data):
    data_mod = []
    plt.title('Task 2 cont')
    for i in data:
        for j in range(10):
            data_mod.append(i / 10)
    plt.hist(

        range(len(data_mod)),
        weights=data_mod,
        edgecolor='black'
    )
    plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
    plt.xlabel('x')
    plt.ylabel('n')
    plt.show()

# Варіаційний ряд для дискретної величини
def print_w_plot(data):
    data_len = len(data)
    plt.title('Task 1 Disc')
    plt.scatter(
        range(data_len),
        data
    )
    plt.plot(range(data_len), data, '-y')
    plt.ylabel('w')
    plt.xlabel('x')
    plt.show()


def print_emp_hist(data):
    ll = len(data)
    plt.title('Emp disc')
    plt.hist(
        range(ll),
        bins=ll,
        weights=data,
        color="black",
        histtype='step',
        edgecolor="black"
    )

    plt.ylabel('n')
    plt.xlabel('x')
    plt.show()


# статистичний розподіл для дискретних
def print_freq_plot(keys, data):
    plt.title('Task 2 Disc')
    plt.hist(
        keys,
        bins=len(keys),
        weights=data,
        edgecolor="black"
    )
    plt.ylabel('n')
    plt.xlabel('x')
    plt.show()


# рахує частотні ймовірності для дискретних
def calc_w_disc(freq_table, amount):
    w_arr = []
    for key, value in freq_table.items():
        w_arr.append(freq_table[key] / amount)
    return w_arr

# рахує частотні ймовірності для неперевних
def calc_w_cont(freq_table, amount):
    res = []
    for i in range(10):
        c = 0
        for j in range(10):
            c += freq_table[i * 10 + j]
        res.append(c / amount)
    return res

# рахує кількість попадань для неперевних
def calc_n_cont(freq_table, amount):
    res = []
    for i in range(10):
        c = 0
        for j in range(10):
            c += freq_table[i * 10 + j]
        res.append(c)
    return res

# повертає dictionary з x і кількості їх появи
def calc_frequency(data):
    return collections.Counter(data)


def calc_emp_disc(data):
    emp_table = [0.0]
    for i in range(100):
        emp_table.append(emp_table[-1] + data[i])
    return emp_table


# повертає кількість класів - 1 з вибріки
def get_r(n):
    i = 0
    while not (pow(2, i) < n <= pow(2, i + 1)):
        i += 1
    return i


# повертає фактичну кількість попадань в клас
def get_m(i, r, data):
    res = 0
    for item in data:
        if (r + 1) * (i - 1) < item <= (r + 1) * i:
            res += 1
    return res


# повертає x емпіричне
def get_x_emp(r, n, f, data):
    res = 0
    for i in range(1, r + 1):
        res += (pow((get_m(i, r, data) - n * get_p(r)), 2)) / n * get_p(r)
    return res


# повертає ймовірність попадання в клас
def get_p(r):
    return 1 / (r + 1)


# розбиває посортовану вибірку на класи
def make_cont_table(data, amount):
    step = amount // (get_r(amount) + 1)
    res = []
    i = 0
    while i < len(data):
        res.append(data[i:i + step])
        i += step
    return res


# повертає список середніх значень в проміжках
def make_count_avg_values(data):
    res = []
    for i in data:
        res.append(np.mean(i))
    return res


# числові характеристики
def numerical_characteristics(data):
    data = np.array(data)
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
    quantil = np.quantile(data, q=[0.25, 0.5, 0.75])
    de = np.quantile(data, q=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
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

    w_arr = calc_w_disc(freq_table, amount)

    print_w_plot(w_arr)
    arr = make_cont_table(data, amount)
    arr = np.array(arr)
    #print(arr)
    #print(calc_w_cont(freq_table, amount))
    res = make_count_avg_values(arr)
    #print(res)
    print_w_hist(calc_w_cont(freq_table, amount))



    emp_table = calc_emp_disc(w_arr)


    k = []
    for i in freq_table.keys():
        k.append(i)
    v = []
    for i in freq_table.values():
        v.append(i)

    print_freq_plot(k, v)
    print_emp_hist(emp_table)


    print_n_hist(calc_n_cont(freq_table, amount))

    print("Дискретні \n")
    numerical_characteristics(data)
    print()
    print("Неперервні \n")
    numerical_characteristics(res)


main()
