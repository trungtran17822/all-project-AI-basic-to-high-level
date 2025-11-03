from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns

data = read_csv('Ecommerce_cleaned.csv',
                sep=',', quotechar='"')
print(data.head())
print(data.shape)