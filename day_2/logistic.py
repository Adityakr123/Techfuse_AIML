import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv('insurance_data.csv')


x = data.drop(columns='bought_insurance',axis=1)
y = data['bought_insurance']
# print(x)
# print(y)

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)


model = LogisticRegression() 
model.fit(x_train,y_train)

pred_x_train = model.predict(x_train)
pred_x_test= model.predict(x_test)
n=len(pred_x_train)
pred_x_train =pred_x_train.reshape((n, 1))
data_accuracy = accuracy_score(pred_x_train,y_train)
data_accuracy_testing = accuracy_score(pred_x_test,y_test)

print(data_accuracy_testing )
# print(data_accuracy)
plt.scatter(x_test,pred_x_test,color='green')
# plt.plot(x_train,pred_x_train,color='blue' )
plt.show()