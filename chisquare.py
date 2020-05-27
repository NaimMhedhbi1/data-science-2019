from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from matplotlib import pyplot
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel('C:/Users/Naim/Desktop/.spyder-py3/LR.xlsx')
X = df.iloc[: , :-1]
Y = df.iloc[: , -1]

"""
chi_scores = chi2(X,Y)
chi_scores
p_values = pd.Series(chi_scores[1],index = X.columns)
p_values.sort_values(ascending = False , inplace = True)
p_values.plot.bar()

"""

from sklearn.feature_selection import f_classif, chi2, mutual_info_classif
from statsmodels.stats.multicomp import pairwise_tukeyhsd
chi2_score, chi_2_p_value = chi2(X,Y)
f_score, f_p_value = f_classif(X,Y)
mut_info_score = mutual_info_classif(X,Y)
pairwise_tukeyhsd = [list(pairwise_tukeyhsd(X[:,i],y).reject) for i in range(10)] 


