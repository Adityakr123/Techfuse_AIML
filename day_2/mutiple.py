import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
df = pd.read_excel("PalmTree.xlsx")
Y=[]

Y=df['Production']

Y = np.array(Y)
# print(Y)
x=[]
x=df['Rainfall']
y=[]
y=df['Temprature']
X=np.empty((len(df), 3), int)
for i in range(len(df)):
     X[i][0]=1
for i in range(len(df)):
    X[i][1]=x[i]
    X[i][2]=y[i]

trans_X = np.transpose(X)
# print(trans_X )
Xnew=np.dot(trans_X,X)
Xnew_inv=np.linalg.inv(Xnew)
Xnewdash=np.dot(trans_X,Y)
B=np.dot(Xnew_inv,Xnewdash)
Ypredict=np.dot(X,B)
for k in range(len(Ypredict)):
    Ypredict[k]=int(Ypredict[k])
Ypredict = pd.DataFrame(Ypredict)
Ypredict = Ypredict.squeeze()
print(Ypredict)


# print(price)


