import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
#reading csv file
dataframe_r=pd.read_csv("heart.csv")
print(dataframe_r.head())
print(dataframe_r.describe())
print(dataframe_r.columns)
print(dataframe_r.info())
#creating heatmap
plt.figure(figsize=(20,10))
sb.heatmap(dataframe_r.corr(),annot=True,cmap='terrain')
#making a pairplot
sb.pairplot(dataframe_r)
dataframe_r.hist(figsize=(11,12))
dataframe_r.plot(kind='pie',subplots=True,figsize=(11,12))
plt.show()
