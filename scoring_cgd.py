import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore') 


#this code is to calculate the diffference between the global median and the median.

df = pd.read_excel('file:///C:/Users/user/.spyder-py3/CJD/scoring_cjd_python.xlsx')

score = df.apply(lambda row:  (row['value'] * row['prct'])/ sum(df.prct),axis=1)
