import matplotlib.pyplot as plt
import numpy as np


def print_plot(data, title='', x_label='', y_label=''):
    keys = list(data.keys())
    values = list(data.values())
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.scatter(keys, values)
    plt.plot(keys, values, '-y')
    plt.show()


def print_histogram(data, title='', x_label='', y_label=''):
    keys = list(data.keys())
    values = list(data.values())
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.bar(keys, values)
    plt.show()


def print_empirical_distribution(data, title='', x_label='', y_label=''):
    keys = list(data.keys())
    values = list(data.values())
    length = len(values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.vlines(keys, 0, values, linestyle="dashed")
    plt.hist(
        range(length),
        bins=length,
        weights=values,
        color="black",
        histtype='step',
        edgecolor="blue")

    plt.show()


def print_cont_hist(freq_table, classes, step, title='', x_label='', y_label=''):
    keys = []
    values = []
    for i in freq_table:
        keys.append(i[0])
        values.append(i[1])
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.hist(
        keys,
        weights=values,
        bins=np.arange(min(classes), max(classes) + step, step),
        align='mid',
        edgecolor='Black',
        color='Yellow'
    )
    plt.xticks(keys)
    plt.show()
