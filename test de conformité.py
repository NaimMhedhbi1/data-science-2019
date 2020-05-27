import pandas as pd 
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation

sns.set(color_codes=True)

df = pd.read_excel('test de conformité.xlsx')
sns.countplot(data = df, x = 'CODE_ENQ')
my_df = pd.crosstab(index = df["CODE_ENQ"],  # Make a crosstab
                              columns=" nbr de qst réalisés")      # Name the count column
my_df.plot.bar()
my_df_1 = my_df/my_df.sum()
