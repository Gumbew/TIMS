import collections
import random

import numpy as np


class Sample:
    def __init__(self, file_name=None):
        if file_name is not None:
            with open(file_name) as file:
                sample = file.readlines()
                self.amount = len(sample)
                self.data = [int(numb) for numb in sample]
                self.data.sort()
                self.a = self.data[0]
                self.b = self.data[-1]

    def write_to_file(self, file_name):
        with open(file_name, "+w") as file:
            for number in self.data:
                file.write(str(number))
                file.write("\n")

    @staticmethod
    def get_r(n):
        i = 0
        while not (pow(2, i) < n <= pow(2, i + 1)):
            i += 1
        return i


class DiscreteSample(Sample):
    def __init__(self, a=0, b=1, amount=10, file_name=None):
        Sample.__init__(self, file_name=file_name)

        if file_name is None:
            self.amount = amount
            self.data = [random.randrange(a, b + 1) for _ in range(amount)]
            self.data.sort()
            self.a = self.data[0]
            self.b = self.data[-1]

        self.__calc_tables()

    def __calc_tables(self):
        self.freq_table = collections.Counter(self.data)
        self.freq_table = collections.OrderedDict(sorted(self.freq_table.items()))

        self.w_table = {}
        for key, value in self.freq_table.items():
            self.w_table[key] = self.freq_table[key] / self.amount

        self.cd_table = {}
        w_sum = 0
        for key, value in self.w_table.items():
            w_sum += value
            self.cd_table[key] = w_sum


class ContinuousSample(Sample):
    def __init__(self, a=0, b=1, amount=10, file_name=None):
        Sample.__init__(self, file_name=file_name)

        if file_name is None:
            self.amount = amount
            self.data = np.random.uniform(a, b, amount)
            self.data.sort()
            self.a = self.data[0]
            self.b = self.data[-1]

        self.__calc_h()
        self.__calc_classes()
        self.__calc_freq_table()

    def __calc_h(self):
        self.h = (self.b - self.a) / (Sample.get_r(self.amount) + 1)

    def __calc_classes(self):
        self.classes = np.linspace(self.a, self.b, Sample.get_r(self.amount) + 2)

    def __calc_freq_table(self):
        self.freq_table = []
        for i in range(1, len(self.classes)):
            count = 0
            for e in self.data:
                if self.classes[i - 1] < e <= self.classes[i]:
                    count += 1
            avg = (self.classes[i] + self.classes[i - 1]) / 2
            self.freq_table.append([avg, count])

        count = 0
        for e in self.data:
            if e == self.classes[0]:
                count += 1
        self.freq_table[0][1] += count
