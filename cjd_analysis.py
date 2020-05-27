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
cjd = pd.read_csv('C:/Users/user/Documents/projets 121 total/CJD/CJD_categ.csv',sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8')
df1 = cjd.melt()
pd.crosstab(index=df1['value'], columns=df1['variable'])
freq_all_cjd = cjd.apply(pd.value_counts)
freq_all_cjd.to_excel('C:/Users/user/.spyder-py3/CJD/cjd_analyse/freq_all_cjd.xlsx') 


cjd_var = []
colN = cjd.columns.tolist()
for column_name in colN : 
    cjd_var = list(cjd[column_name].value_counts() )
    cjd_var.append(pd.DataFrame(data=cjd_var,name=column_name))
"""maxlen = 0
for column_name in cjd_var:
    if len(column_name) > maxlen:
        maxlen = len(column_name)

fillerData = np.empty((maxlen,len(colN),))
dfDiff = pd.DataFrame(columns=colN,data=fillerData)

for i in range(len(cjd_var)):
    dfDiff[colN[i]] = cjd_var[i]    
    

""" 
    
cjd_cjd = cjd.apply(pd.value_counts).fillna(0)
cjd_cjd = cjd_cjd.dropna(axis = 1, how ='all')
cjd_cjd .to_excel('C:/Users/user/.spyder-py3/CJD/cjd_analyse/cjd_cjd .xlsx') 






