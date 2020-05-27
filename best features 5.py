# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:09:05 2020

@author: Naim
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel('C:/Users/Naim/Desktop/.spyder-py3/LR.xlsx')
X = df.iloc[: , :-1]
Y = df.iloc[: , -1]


import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,Y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()
