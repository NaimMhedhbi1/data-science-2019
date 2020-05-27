import numpy as np 
import pandas as pd 

df = pd.read_excel('file:///C:/Users/user/Documents/projets 121 total/RE/RE 16_01.xlsx')


#df['duration11']= pd.to_datetime(df.duration_1, format='%H%M').dt.time
df1 = pd.DataFrame() 
colN = df.columns.tolist()    
for each in colN: 
   temp = pd.to_datetime(df[each], format='%H%M').dt.time
   df1 = df1.append(temp)


"""d = []
for p in game.players.passing():
    d.append((p, p.team, p.passer_rating()))


df1 = pd.DataFrame()
for each in df.columns.tolist() :
    df1 = df1.append({df1[each]: pd.to_datetime(df[each], format='%H%M').dt.time }, ignore_index=True)

d = {}
for name in df.columns.tolist():
    d[name] = pd.DataFrame() 
    d[name] = pd.to_datetime(df[name], format='%H%M').dt.time
"""    