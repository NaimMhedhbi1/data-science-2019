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
survey_data = pd.read_excel('CJD.xlsx' , sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8' )
ccc = pd.read_excel('ccc1.xlsx' , sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8' )
#ccc = ccc.drop_duplicates(['Q8Other1', 'Q8Other2','Q8Other3', 'Q8Other4'])


df = pd.read_excel('ccc1.xlsx' , sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8' )

def get_coded_values(x) :
    colN = x.columns.values
    for column_name in colN:
        i, r = pd.factorize(pd.DataFrame((x[column_name]).unique()).set_axis(['Unique_Values'], axis=1, inplace=False).Unique_Values)
        choices = np.arange(max(len(x[column_name]), r.size))
        c = np.random.choice(choices, r.shape, False)
        x[column_name] = pd.DataFrame((x[column_name]).unique()).set_axis(['Unique_Values'], axis=1, inplace=False).assign(
        Unique_Values=c[i])
        y = x[column_name]

    return y

df1 = df
colN = df1.columns.values
for column_name in colN:
    dummies = get_coded_values(df1)
    col_names_dummies = dummies.columns.values


for i,value in enumerate(col_names_dummies):
        df1[value] = dummies.iloc[:,i]


"""create unique values from the first dataframe****RUN IN CONSOLE****"""
colNames = ccc.columns.tolist()
uniqueValsList = []

for each in colNames:
    uniqueVals = list(ccc[each].unique())
    uniqueValsList.append(pd.Series(data=uniqueVals,name=each))

maxlen = 0
for each in uniqueValsList:
    if len(each) > maxlen:
        maxlen = len(each)

fillerData = np.empty((maxlen,len(colNames),))
dfDiff = pd.DataFrame(columns=colNames,data=fillerData)

for i in range(len(uniqueValsList)):
    dfDiff[colNames[i]] = uniqueValsList[i]
       
dfDiff.to_excel('dfDiff.xlsx', index = True)

frames = [ccc,dfDiff,df1]
result = pd.concat(frames, axis = 1 )  
result.to_excel('result.xlsx', index = True)

"""new = df.columns.tolist()
length = len(new)

#for column_name, column in df.transpose().iterrows():
grades = []
for column in df.columns :
    for j in range(length) :

        grades[j].append(df[column].unique() ,axis=1, inplace=False)
        df['grades'][j] = grades"""
"""
Q8_other_c = (survey_data['Q8Other1']).unique()
Q8_other_cd= pd.DataFrame(Q8_other_c).set_axis([ 'Unique_Values'], axis=1, inplace=False)
Q8_other_c = (survey_data['Q8Other2']).unique()
Q8_other_cdd= pd.DataFrame(Q8_other_c).set_axis([ 'Unique_Values'], axis=1, inplace=False)

i, r = pd.factorize(Q8_other_cd.Unique_Values)
choices = np.arange(max(124, r.size))
c = np.random.choice(choices, r.shape, False)
Q8_other_cd['c'] = Q8_other_cd.assign(Unique_Values=c[i])
Q8_other_cd.to_excel('Q8_other_cd.xlsx') """




""" while i < length:
    print(list[i])
    i += 1 
    .set_axis([ 'Unique_Values'], axis=1, inplace=False
    """
#comments : #########
#df = pd.read_csv("pg.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8')
#Q8_other_c = (survey_data['Q8Other1'].append( survey_data['Q8Other2'])).unique()
#Q8_other_c = pd.DataFrame(Q8_other_c)     #############
