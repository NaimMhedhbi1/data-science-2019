import pandas as pd 
import numpy as np 

df = pd.read_excel('taux_refus.xlsx')

"calculate the missing values in each row "
for i in range(len(df.index)) :
    
    print("Nan in row ", i , " : " ,  df.iloc[i].isnull().sum())
    
Qst_réalisés_par_enq = df['Agent'].value_counts()    
#df['NSP_sum'] = (df[[]] == '8').sum(axis=1)
#You may check melt + crosstab
"calculate the frequency of each value in each row par ENQUETEUR"
newdf=df.melt('Agent')
freq_NSP_parENQ = pd.crosstab(newdf.Agent,newdf.value.fillna('NAN'))
freq_NSP_parENQ_nan = freq_NSP_parENQ['NAN']

"calculate the frequency of each value in each row par ID"
newdf=df.melt('id')
freq_NSP_parID = pd.crosstab(newdf.id,newdf.value.fillna('NAN'))
freq_NSP_parID_nan = freq_NSP_parID['NAN']
#df_info= df[['QID','Q1202','Q1205','Q1206','Q1207','Q1208','Q1210','Q1211','Q1213','Q326']]

Qst_réalisés_par_enq = df['Agent'].value_counts() 

