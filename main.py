import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import moment

d = pd.read_csv('info.csv', sep=',')
plt.style.use('ggplot')
df = pd.DataFrame(d, columns=['name', 'values'])
df['values'] /= 1000
df = df.sort_values(by=['values'], ascending=False)

df.to_csv('out.txt', sep='\t')
f = open('out.txt', 'a')
f.write('Frequency Table')
crosstab = pd.crosstab(index=df["values"],
                       columns="count",)
crosstab.to_csv('out.txt', mode='a', sep='\t', header=None)

mode = df['values'].mode()
print('mode', mode)
mean = df['values'].mean()
print('mean', mean)
median = df['values'].median()
print('median', median)
max = df['values'].max()
print('max', max)
min = df['values'].min()
print('min', min)
range = max - min
print('range', range)
variansa = df['values'].var(axis=None)
print('var', variansa)
fluct = variansa**0.5
print('fluct', fluct)
variatsiya = fluct/mean
print('Variatsiya',variatsiya)
quantil = df['values'].quantile(q=[0.25, 0.5, 0.75])
print('qua', quantil)
de = df['values'].quantile(q=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print('de', de)
# asymetriya
asm = df['values'].skew(axis=None)
print('asym', asm)
eks = df['values'].kurtosis(axis=None)
print('eks', eks)

IDR = de.values[8]-de.values[0]
print('IDR', IDR)
print('moments: ',moment(df['values'],axis=None,moment=[0,1,2,3,4]))




iqr = quantil.values[2]-quantil.values[0]
print('IQR',iqr)

#print(crosstab['col_0'])

