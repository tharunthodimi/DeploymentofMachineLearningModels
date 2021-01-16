# libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle

data=pd.read_csv('car data.csv')
data.head()

data=data.iloc[:,1:]
data.head()

data['Currentyear']=2020

data.head()

data['no_year']=data['Currentyear']-data['Year']

data.head()

data.drop(['Year','Currentyear'],axis=1,inplace=True)

data.head()

data=pd.get_dummies(data,drop_first=True)
data.head()

y=data.iloc[:,:1]
y

x=data.iloc[:,1:]
x

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
y_pred
print(y_pred)

#prediction on user provide data
'''
lr.predict([[5.59,24000,0,6,0,1,0,1]])

pickle.dump(lr,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
'''
