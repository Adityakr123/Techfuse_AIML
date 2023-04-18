import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
df = pd.read_excel("PalmTree.xlsx")
Y=[]

Y=df['Production']

Y = np.array(Y)
# print(Y)
x=[]
x=df['Rainfall']
y=[]
y=df['Temprature']
z=[]
z=df['Area']
X=np.empty((len(df), 4),float)
for i in range(len(df)):
     X[i][0]=1
for i in range(len(df)):
    X[i][1]=x[i]
    X[i][2]=y[i]
    X[i][3]=z[i]
# print(X)
trans_X = np.transpose(X)
# print(trans_X )
Xnew=np.dot(trans_X,X)
Xnew_inv=np.linalg.inv(Xnew)
Xnewdash=np.dot(trans_X,Y)
B=np.dot(Xnew_inv,Xnewdash)
Ypredict=np.dot(X,B)
# print(B)
x1=float(input("Enter Rainfall"))
x2=float(input("Enter Area"))
x3=float(input("Enter Temprature"))
price=B[0]+(B[1]*x1)+(B[2]*x3)+(B[3]*x2)
print(price)
print(B[0],B[1],B[2],B[3])
# plt.scatter(x,Y,color='orange' )
# plt.scatter(y,Y,color='Red' )
# plt.scatter(x,Ypredict,color='green')
# plt.scatter(y,Ypredict,color='blue' )
# plt.show()

# print(Ypredict)


