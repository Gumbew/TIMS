import math

import numpy as np
from scipy import stats

from sample import DiscreteSample


class SampleStats:
    def __init__(self, sample: DiscreteSample):
        self.sample = sample
        self.update()

    def update(self):
        self.__calc_expected_value()
        self.__calc_dispersion()
        self.__calc_standard_deviation()
        self.__calc_average()
        self.__calc_mode()
        self.__calc_median()
        self.__calc_quartiles()
        self.__calc_deciles()
        self.__calc_swing()
        self.__calc_variance()
        self.__calc_standard()
        self.__calc_variation()
        self.__calc_quartile_width()
        self.__calc_decile_width()
        self.__calc_skew()
        self.__calc_kurtosis()

    def print(self):
        print('Мат. сподівання: ', self.expected_value)
        print('Дисперсія: ', self.dispersion)
        print('Стандартне відхилення: ', self.standard_deviation)
        print('Середнє значення: ', self.average)
        print('Мода: ', self.mode)
        print('Медіана: ', self.median)
        print('Квартилі: ', self.quartiles)
        print('Децилі: ', self.deciles)
        print('Розмах: ', self.swing)
        print('Варіанса: ', self.variance)
        print('Стадндарт: ', self.standard)
        print('Варіація: ', self.variation)
        print('Інтерквартильна широта: ', self.quartile_width)
        print('Інтердецильна широта: ', self.decile_width)
        print('Асиметрія: ', self.skew)
        print('Ексцес: ', self.kurtosis)

    def __calc_expected_value(self):
        self.expected_value = 0
        for key, value in self.sample.w_table.items():
            self.expected_value += key * value

    def __calc_dispersion(self):
        self.dispersion = 0
        for key, value in self.sample.w_table.items():
            self.dispersion += key * key * value
        self.dispersion -= self.expected_value * self.expected_value

    def __calc_standard_deviation(self):
        self.standard_deviation = math.sqrt(self.dispersion)

    def __calc_average(self):
        self.average = 0
        for key, value in self.sample.freq_table.items():
            self.average += key * value
        self.average /= self.sample.amount

    def __calc_mode(self):
        self.mode = self.sample.a
        max_freq = 0
        for key, value in self.sample.freq_table.items():
            if value > max_freq:
                self.mode = key
                max_freq = value

    def __calc_median(self):
        amount = self.sample.amount
        data = self.sample.data
        if amount % 2 == 1:
            self.median = data[amount // 2]
        else:
            self.median = (data[amount // 2 - 1] + data[amount // 2]) / 2

    def __calc_quartiles(self):
        if self.sample.amount % 4 == 0:
            self.quartiles = []
            for i in range(1, 4):
                self.quartiles.append(self.sample.data[(self.sample.amount // 4) * i - 1])
        else:
            self.quartiles = None

    def __calc_deciles(self):
        if self.sample.amount % 10 == 0:
            self.deciles = []
            for i in range(1, 10):
                self.deciles.append(self.sample.data[(self.sample.amount // 10) * i - 1])
        else:
            self.deciles = None

    def __calc_swing(self):
        self.swing = max(self.sample.data) - min(self.sample.data)

    def __calc_variance(self):
        self.variance = 0
        for value in self.sample.data:
            self.variance += (value - self.average) ** 2
        self.variance /= self.sample.amount - 1

    def __calc_standard(self):
        self.standard = math.sqrt(self.variance)

    def __calc_variation(self):
        self.variation = self.standard / self.average

    def __calc_quartile_width(self):
        if self.quartiles is not None:
            self.quartile_width = self.quartiles[-1] - self.quartiles[0]
        else:
            self.quartile_width = None

    def __calc_decile_width(self):
        if self.deciles is not None:
            self.decile_width = self.deciles[-1] - self.deciles[0]
        else:
            self.decile_width = None

    def __calc_skew(self):
        self.skew = stats.skew(np.array(self.sample.data))

    def __calc_kurtosis(self):
        self.kurtosis = stats.kurtosis(self.sample.data)
