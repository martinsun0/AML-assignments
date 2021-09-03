# %% Q2
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# Read CSV from file
df = pd.read_csv(r'C:\Users\marti\PycharmProjects\AML-assignments\hw0\iris.data',
                 names=['Sepal-Length(cm)', 'Sepal-Width(cm)', 'Petal-Length(cm)', 'Petal-Width(cm)', 'class'])

# Index the attributes and species matrices
attributes = df[['Sepal-Length(cm)', 'Sepal-Width(cm)', 'Petal-Length(cm)', 'Petal-Width(cm)']]
species = df[['class']]

# %% Q3

# Create and save a seaborn pair-plot
g = sns.pairplot(df, hue='class')
g.fig.suptitle('Iris Data PairPlots', y=1)
plt.show()
plt.savefig("pair-plot.svg")
