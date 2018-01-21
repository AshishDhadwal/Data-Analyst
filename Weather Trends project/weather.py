# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

# Importing files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('weather.csv')
def simplifiedRollingMean(windowRolling, dataset_i):
    dataset_o = dataset_i.rolling(window = windowRolling, center=False, on = "year").mean().dropna()
    return dataset_o

# Calculation
rollingWindow = 10
df_movingAverage = simplifiedRollingMean(rollingWindow,dataset)


# Draw graph in matplotlib
plt.plot(df_movingAverage['year'], df_movingAverage['city_avg_temp'], label='Delhi')
plt.plot(df_movingAverage['year'], df_movingAverage['global_avg_temp'], label='Global')
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Delhi vs Global values ({} year moving avg)".format(rollingWindow))
plt.show()


