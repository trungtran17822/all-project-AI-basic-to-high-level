from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = read_csv('salary_employment.csv')
print(data.head())
print(data.shape)
print(data[data.duplicated()])

