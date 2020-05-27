import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel('C:/Users/Naim/Desktop/.spyder-py3/LR_label.xlsx')
x1 = df.iloc[: , :-1]
Y = df.iloc[: , -1]

from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder

onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(x1.astype(str)).toarray()


from sklearn.feature_selection import f_classif, chi2, mutual_info_classif
from statsmodels.stats.multicomp import pairwise_tukeyhsd
chi2_score, chi_2_p_value = chi2(X,Y)
f_score, f_p_value = f_classif(X,Y)
mut_info_score = mutual_info_classif(X,Y)
pairwise_tukeyhsd = [list(pairwise_tukeyhsd(X[:,i],Y).reject) for i in range(10)] 