from ctypes import sizeof
import pandas as pd
from random import randint
import numpy as np
import statistics as st
from operator import itemgetter
df = pd.read_csv('KNN.csv')
import csv
A = list(csv.reader(open('KNN.csv')))
x=input("enter name:")
x1=float(input("enter age:"))
x2=float(input("enter income in K:"))
x3=float(input("enter no of creditcards person has:"))
a=[x1,x2,x3]
k=len(df)-1
if k%2==0:
    k=k-1
arr=np.empty((len(df),2),float)
# print(np.shape(arr))

for i in range(1,len(df)+1):
    count=0
    sum=0
    for j in range(1,4):
        count=a[j-1]-int(A[i][j])
        # print(A[i][j])
        count=pow(count,2)
        sum=sum+count
    sum=pow(sum,1/2)
    # print(sum)
    if A[i][4]=='Yes':
        arr[i-1][0]=1
    else:
        arr[i-1][0]=0
    # print(A[i][4])
    arr[i-1][1]=sum
# print(arr)
arr=sorted(arr, key=itemgetter(1))
# print(arr)
yescount=0
nocount=0
for i in range(k):
    if arr[i][0]==1:
        yescount=yescount+1
    else:
        nocount=nocount+1
if yescount>nocount:
    print("yes")
else:
    print("no")
# print(arr)
