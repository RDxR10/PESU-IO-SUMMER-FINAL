#===========================================================================================================
#Accuracy = 0.83065 (83.06%)
#===========================================================================================================
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:08:18 2019

@author: RDxR10
"""

import pandas as pd  
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('combined_city_data.csv')
df=df.fillna(method='ffill')
df = df.drop(columns=['Date','Location','Sunshine','Evaporation','Cloud3pm','Cloud9am','RISK_MM','WindGustDir', 'WindDir3pm', 'WindDir9am'],axis=1)
df.dropna()

#Basis for classification
df['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
df['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)


X = df[['Humidity3pm','Humidity9am','Pressure3pm','Pressure9am','MinTemp','MaxTemp','Temp3pm','Temp9am','Rainfall','RainToday']]
y = df[['RainTomorrow']]

#Preprocessing
s = preprocessing.MinMaxScaler()
s.fit(df)



#Extracting Relevant features using heatmap: 
corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
p1=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")
print(p1)


X = df[['Humidity3pm','Rainfall','RainToday']]

#Random Sampling
df = df.sample(frac=1)


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
LR = LogisticRegression(solver='liblinear')
LR.fit(X_train,y_train.values.ravel())
y_RF = LR.predict(X_test)
accuracy = accuracy_score(y_test,y_RF)

print('Accuracy :',accuracy,'\n')

cm=confusion_matrix(y_test,y_RF)
print('Confusion Matrix : ','\n')
print(cm)
#plt.figure(figsize=(5,5))
#p2=sns.heatmap(cm, fmt='d', cmap='GnBu', cbar=False, annot=True)
#print(p2)

