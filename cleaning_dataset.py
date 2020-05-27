import pandas as pd 
import numpy as np 

df = pd.read_excel('AM 20-05-2020.xlsx') 
"""
value_counts = df.apply(pd.value_counts)

df1 = pd.crosstab(df['name'], df['code'].fillna('n/a'))
for i in df.columns:
    x = df[i].value_counts()
    print("Column name is:",i,"and it value is:",x)
    print()
""" 
# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Reading the data

print(df.shape)
print(df.info())    
describe = df.describe()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print(df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
 

            
                  
                  
    
