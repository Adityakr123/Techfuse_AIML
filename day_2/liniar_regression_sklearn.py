
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import timeit
import time

data = pd.read_csv("headbrain.csv")
X = data.drop(columns='Brain Weight', axis=1)
Y = data['Brain Weight']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

print(X.shape, X_train.shape, X_test.shape)

selected_model = LinearRegression()

selected_model.fit(X_train, Y_train)


Y_train_prediction = selected_model.predict(X_train)
n=len(X_train)
Y_train_prediction = Y_train_prediction.reshape((n, 1))
print(X_train.shape,Y_train_prediction.shape )



plt.scatter(X_train,Y_train,color='red' )
plt.scatter(X_train,Y_train_prediction,color='green')
plt.plot(X_train,Y_train_prediction,color='blue' )
plt.show()
# def liniar_regression_with():
#     data = pd.read_csv("headbrain.csv")
#     X = data.drop(columns='Brain Weight', axis=1)
#     Y = data['Brain Weight']
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
#     selected_model = LinearRegression()
#     selected_model.fit(X, Y)
#     Y_train_prediction = selected_model.predict(X)
#     n=len(X)
#     for i in range(len(Y_train_prediction)):
#         Y_train_prediction[i]=int(Y_train_prediction[i])

#     # Y_train_prediction = Y_train_prediction.reshape((n, 1))
#     plt.scatter(X,Y,color='red' )
#     plt.scatter(X,Y_train_prediction,color='green')
#     plt.plot(X,Y_train_prediction,color='blue' )
#     # print(Y.shape,Y_train_prediction.shape)
#     print('accuracy score: ',accuracy_score(Y,Y_train_prediction))
#     # plt.show()


# liniar_regression_with()

   



# print('Time Used :',)
# print ('Space ', )
