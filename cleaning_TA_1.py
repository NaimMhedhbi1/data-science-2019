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
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/user/.spyder-py3/TA.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
#mydateparser = lambda x: pd.datetime.strptime(x, "%m/%d/%y")
#df = pd.read_csv("C:/Users/user/.spyder-py3/TA5.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode', parse_dates=['START_TIME'],
#date_parser=mydateparser)
#convert from string to datetime
df['END_TIME']= pd.to_datetime(df['END_TIME'] , errors = 'coerce')
df['START_TIME']= pd.to_datetime(df['START_TIME'], errors = 'coerce')
df['diff_hours'] = df['END_TIME'] - df['START_TIME']
#difference_hours is the variable that was created in order 
#to extract the values below the 50%  of the median 
df['difference_hours'] = df['diff_hours']/np.timedelta64(1,'h') 
df['diff_hours']= pd.to_datetime(df['diff_hours'] , errors = 'coerce')
# selecting rows based on condition +
#0.16205 is the 50% of the median 
df ['START_TIME_1'] =  df ['START_TIME'].dt.time
df['END_TIME_1'] =  df['END_TIME'].dt.time
df['diff_hours_1'] = df ['diff_hours'].dt.time
frd = df.loc[df['difference_hours'] <0.162025]
df= df.set_index(df['QID'])

#since variables were stored as a timestamp we should always change the date (2019-10-15)
#update it whenever we wanna use this code
frd_after_9pm = df.loc[df['START_TIME'] > '2019-10-15 21:00:00']
frd_before_7_am = df.loc [df['START_TIME'] < '2019-10-15 07:00:00']
#using this part of code to split time from datetime object 

#frd_info is the dataset that contains all the informations
# neccessary of the sup or enq who is not doing well

frd_after_9pm_info = frd_after_9pm[['QID','GENRE','DATE','START_TIME_1','END_TIME_1','diff_hours_1','GOUVERNORAT','DELEGATION','SECTEUR','MILIEU','CODE_ENQ','NOM_ENQ','CODESUP','NOMSUP']]
frd_before_7_am_info = frd_before_7_am[['QID','GENRE','DATE','START_TIME_1','END_TIME_1','diff_hours_1','GOUVERNORAT','DELEGATION','SECTEUR','MILIEU','CODE_ENQ','NOM_ENQ','CODESUP','NOMSUP']]
frd_info = frd[['QID','GENRE','DATE','START_TIME_1','END_TIME_1','diff_hours_1','GOUVERNORAT','DELEGATION','SECTEUR','MILIEU','CODE_ENQ','NOM_ENQ','CODESUP','NOMSUP']]

## Select duplicate rows except first occurrence based on all columns
duplicateRowsDF = df[df.duplicated()] 
#Find Duplicate Rows based on selected columns
duplicateRowsDF1 = df[df.duplicated(['QID'])]
duplicateRowsDF2 = df[df.duplicated(['TEL'])]

frd.to_excel('frd.xlsx') 
frd_info.to_excel('frd_info.xlsx')
frd_before_7_am_info.to_excel('frd_before_7_am_info.xlsx')
frd_after_9pm_info.to_excel('frd_after_9pm_info.xlsx')

def check_date_by_id(df):

    df['prevFrom'] = df['START_TIME'].shift()
    df['prevTo'] = df['END_TIME'].shift()

    def check_date_by_row(x):

        if pd.isnull(x.prevFrom) or pd.isnull(x.prevTo):
            x['overlap'] = False
            return x

        latest_start = max(x['START_TIME'], x.prevFrom)
        earliest_end = min(x['END_TIME'], x.prevTo)
        x['overlap'] = int((earliest_end - latest_start).time) + 1 > 0
        return x

    return df.apply(check_date_by_row, axis=1)
 
df['ovrlp'] = df.groupby('QID').apply(check_date_by_id)

   
