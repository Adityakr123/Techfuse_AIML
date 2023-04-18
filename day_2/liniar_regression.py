import pandas as pd
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
def liniar_regression_without():
    df = pd.read_csv("headbrain.csv")
    x = df['Head Size']
    y = df['Brain Weight']
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    covar_var = 0
    for i in range(len(x)):
        covar_var+=(x[i]-mean_x)*(y[i]-mean_y)
    covar = covar_var/(len(x)-1)
    temp=0
    for i in x:
        temp+=((i-mean_x)**2)
    var = temp/(len(x) -1)
    arr=[]
    weight = covar/var
    bias = mean_y - (weight*mean_x)
    plt.scatter(x,y,color='red')
    for i in x:
        j=(weight*i)+bias
        arr.append(int(j))
    # plt.scatter(x,arr,color='green')
    # plt.plot(x,arr,color='blue' )
    # plt.show()
    y_predict = pd.DataFrame(arr)
    y_predict = y_predict.squeeze()
    # cf_matrix = confusion_matrix(y,y_predict)
    # print(cf_matrix)
    # print(y,y_predict)
    # print('accuracy score :',accuracy_score(y,y_predict))
liniar_regression_without()