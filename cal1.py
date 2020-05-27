import numpy as np 
import pandas as pd 
df= pd.read_excel('C:/Users/user/.spyder-py3/Manipulaion_home/calmedian.ods.xlsx')
xmd = 121
df1 = pd.DataFrame() 
colN = df.columns.tolist()

    
for each in colN : 
       df1[each] = df[each] - xmd
