
import pandas as pd 
import numpy as np 

df = pd.read_excel('27_01.xlsx')


p_match = df.loc[df['QID'].isin(['975','927','1415','1408','1032','1031','971','972','1040','1039','928','979','976','975','980'])]
p_match_info = p_match[['QID','Q1209','Q1206','Q1204','Q1216','DURATION','NR','NS','BID']]

for i in range(len(df.index)) :
    
    print("Nan in row ", i , " : " ,  df.iloc[i].isnull().sum())
    
"calculate the frequency of each value in each row par ID"
newdf=df.melt('QID')
freq_NSP_parID = pd.crosstab(newdf.QID,newdf.value.fillna('NAN'))
freq_NSP_parID_nan = freq_NSP_parID['NAN']
df_info= df[['QID','Q1202','Q1205','Q1206','Q1207','Q1208','Q1210','Q1211','Q1213','Q326']]
