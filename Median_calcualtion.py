#invite people for the Kaggle party
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
from datetime import datetime, date, time
import datetime as dt
from time import mktime as mktime 
from collections import namedtuple 

import warnings
warnings.filterwarnings('ignore') 

#this code is to calculate the diffference between the global median and the median.

df = pd.read_excel("C:/Users/user/.spyder-py3/Manipulaion_home/Median_calcualtion.ods")
""" median_1 = 51 

df['diff'] = df.apply(lambda row:  median_1  - row['DURATION_2'] ,axis=1)
df1 = df[['Enq','DURATION_2','diff']] 
df1.to_excel('C:/Users/user/.spyder-py3/Arab_Index/df2.xlsx') 
""""
"""a sample dictionary
data = {'x1':[1,0,4,5,8,1], 
     'x2':[3,4,5,6,8,9],
     'x3':[4,5,1,-2,4,5]} 
df = pd.DataFrame(data) #converting the dictionary to dataframe """

