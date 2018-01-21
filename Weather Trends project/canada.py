# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:40:22 2018

@author: Ashish
"""

# Importing files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('weather.csv')
def simplifiedRollingMean(windowRolling, dataset_input):
    dataset_output = dataset_input.rolling(window = windowRolling, center=False, on = "year").mean().dropna()
    return dataset_output

# Calculation
rollingWindow = 10
df_movingAverage = simplifiedRollingMean(rollingWindow,dataset)


# Draw graph in matplotlib
plt.plot(df_movingAverage['year'], df_movingAverage['city_avg_temp'], label='Delhi')
plt.plot(df_movingAverage['year'], df_movingAverage['global_avg_temp'], label='Global')
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Delhi vs Global Temp ( moving avg {} year)".format(rollingWindow))
plt.show()
