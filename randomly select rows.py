import pandas as pd 
import numpy as np 

df = pd.read_excel('C:/Users/Naim/Documents/sample 05-02-2020.xlsx')
df_1 = df.sample( frac = 0.50)