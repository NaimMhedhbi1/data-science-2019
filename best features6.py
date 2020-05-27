
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel('C:/Users/Naim/Desktop/.spyder-py3/LR.xlsx')
X = df.iloc[: , :-1]
Y = df.iloc[: , -1]

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

lr =LogisticRegression()
lr.fit(X_train, Y_train)
mul_lr = LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(X_train , Y_train)
    
