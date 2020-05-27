#invite people for the Kaggle party
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
from datetime import datetime, date, time , timedelta
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/user/.spyder-py3/pg_tun_803.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode' , encoding = 'UTF-8')

df['END_TIME']= pd.to_datetime(df['END_TIME'] , errors = 'coerce')
df['START_TIME']= pd.to_datetime(df['START_TIME'], errors = 'coerce')
df['diff_hours'] = df['END_TIME'] - df['START_TIME']
df['difference_hours'] = df['diff_hours']/np.timedelta64(1,'h')
h_median = (df['difference_hours'].median()) * 0.5 ; 
df['diff_hours']= pd.to_datetime(df['diff_hours'] , errors = 'coerce')
df ['START_TIME_1'] =  df ['START_TIME'].dt.time
df['END_TIME_1'] =  df['END_TIME'].dt.time
df['diff_hours_1'] = df ['diff_hours'].dt.time
frd = df.loc[df['difference_hours'] < h_median]
df= df.set_index(df['QID'])


frd_after_9pm = df.loc[df['START_TIME'] > '2019-10-21 21:00:00']
frd_before_7_am = df.loc [df['START_TIME'] < '2019-10-21 07:00:00']
frd_after_9pm_info = frd_after_9pm[['QID','DATE','START_TIME_1','END_TIME_1','diff_hours_1','D4','D3A','D3B','D3C','NAME_ENUMERATOR','NAME_SUPERVISOR']]
frd_before_7_am_info = frd_before_7_am[['QID','DATE','START_TIME_1','END_TIME_1','diff_hours_1','D4','D3A','D3B','D3C','NAME_ENUMERATOR','NAME_SUPERVISOR']]
frd_info = frd[['QID','DATE','START_TIME_1','END_TIME_1','diff_hours_1','D4','D3A','D3B','D3C','NAME_ENUMERATOR','NAME_SUPERVISOR']]

occur = df['NAME_ENUMERATOR'].value_counts()
## Select duplicate rows except first occurrence based on all columns
duplicateRowsDF = df[df.duplicated()] 
#Find Duplicate Rows based on selected columns
duplicateRowsDF1= df[df.duplicated(['QID'])]
duplicateRowsDF2 = df[df.duplicated(['D17'])]
duplicateRowsDF1_info =duplicateRowsDF1[['NAME_SUPERVISOR','NAME_ENUMERATOR','D17']] 
duplicateRowsDF2_info =duplicateRowsDF2[['NAME_SUPERVISOR','NAME_ENUMERATOR','D17']] 
#duplicateRowsDF2_info['description'] = duplicateRowsDF2_info.groupby(['NOM_SUPERVISEUR', 'NOM_ENQUETEUR' ]).reset_index()
#duplicateRowsDF2_info['description'] = duplicateRowsDF2_info['NOM_SUPERVISEUR','NOM_ENQUETEUR'].apply( lambda x,y : groupby(x , y)).reset_index()
#group_by_carrier = duplicateRowsDF2_info['D17'].groupby(['NOM_SUPERVISEUR','NOM_ENQUETEUR']).agg(['count'])  
#group_by_carrier_size= group_by_carrier.size() 
duplicate_counts= duplicateRowsDF2_info.groupby(['NAME_SUPERVISOR','NAME_ENUMERATOR'])['D17'].count()
duplicate_counts_1= duplicateRowsDF2_info.groupby(['NAME_ENUMERATOR'])['D17'].count()
#duplicateRowsDF2_info['duplicate_counts_1'] = duplicate_counts_1 
#duplicateRowsDF2_info['occur'] = occur 
occur = df['NAME_ENUMERATOR'].value_counts()
dDF2_info = pd.DataFrame.from_items([('occur', occur), ('duplicate_counts_1',duplicate_counts_1)])
#duplicateRowsDF2_info = duplicateRowsDF2_info.assign(duplicate_counts= duplicateRowsDF2_info.groupby(['NOM_SUPERVISEUR','NOM_ENQUETEUR'])['D17'].count()).reset_index(level=0, drop=True)
#duplicateRowsDF2_info = duplicateRowsDF2_info.assign(duplicate_counts=pd.Series(np.random.randn(len(duplicate_counts))).values)

        


frd.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/frd.xlsx') 
duplicateRowsDF1_info.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/duplicateRowsDF1_info.xlsx')
frd_info.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/frd_info.xlsx')
frd_before_7_am_info.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/frd_before_7_am_info.xlsx')
frd_after_9pm_info.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/frd_after_9pm_info.xlsx')
duplicate_counts.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/duplicate_counts.xlsx', index = True)
dDF2_info.to_excel('C:/Users/user/.spyder-py3/pg30_tunisie/dDF2_info.xlsx', index = True)
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

    return df.apply(check_date_by_row, axis=1).drop(['prevFrom','prevTo'], axis=1)
 
df = df.groupby('QID').apply(check_date_by_id)

#What I want is to find where the ranges in df2 have overlap with 
#the ranges in df1, how long that overlap is (in seconds), and what
#value of df2.catg that is. I want the length of that overlap inserted
#into a column in df1
#(that column will be named for the catg it represents).
def main(df):
    for cat in df.NAME_ENUMERATOR.unique().tolist():
        df[cat] = 0
    it1 = df.iterrows()
    it2 = df.iterrows()
    idx1, row1 = next(it1)
    idx2, row2 = next(it2)
    while True:
        try:
            r1 = range(start=row1.START_TIME, end=row1.END_TIME)
            r2 = range(start=row2.START_TIME, end=row2.END_TIME)
            if r2.end < r1.start:
                # no overlap. r2 before r1. advance it2
                idx2, row2 = next(it2)
            elif r1.end < r2.start:
                # no overlap. r1 before r2. advance it1
                idx1, row1 = next(it1)
            else:
                # overlap. overlap(row1, row2) must > 0 
                df.loc[idx1, row2.NAME_ENUMERATOR] += overlap(row1, row2)
                # determine whether to advance it1 or it2
                if r1.end < r2.end:
                    # advance it1
                    idx1, row1 = next(it1)
                else:
                    # advance it2
                    idx2, row2 = next(it2)
        except StopIteration:
            break

main(df)