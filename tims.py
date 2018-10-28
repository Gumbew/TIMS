import collections
import os.path
import random

import matplotlib.pyplot as plt
import numpy as np


def gen_data(file_name, amount):
    if os.path.isfile(file_name):
        return
    _data = [random.randrange(0, 100) for i in range(amount)]
    f = open(file_name, '+w')
    for element in _data:
        f.write("%s\n" % element)


def read_data(file_name):
    _data = []
    f = open(file_name)
    for element in f.readlines():
        _data.append(int(element))
    return _data


data_file = "heh.data"
gen_data(data_file, 1000)
data = read_data(data_file)

data = np.array(data)
data = np.sort(data)

freq_table = collections.Counter(data)


w_arr = []
for key, value in freq_table.items():
    w_arr.append(freq_table[key] / 1000)

plt.plot(freq_table.keys(),w_arr)
plt.show()
plt.hist(freq_table.keys(),freq_table.values())
plt.show()
print(w_arr)
