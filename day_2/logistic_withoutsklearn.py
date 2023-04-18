import random
import csv
import pandas as pd
import numpy as np
df=pd.read_csv("insurance_data.csv")
A = list(csv.reader(open('insurance_data.csv')))
# print(A)
e=2.71828
arr_0=[]
arr_1=[]
beta=random.uniform(0,1)
for i in range(1,len(df+1)):
    if A[i][1]=='1':
        arr_1.append(int(A[i][0]))
    else:
        arr_0.append(int(A[i][0]))
product_0=0
beta_old=0
product=1
while(product_0<product):
    for i in range(1,len(arr_0)):
        sum=1-(1/(1+(pow(e,-(beta*(arr_0[i]))))))
        product=product*sum
    for i in range(1,len(arr_1)):
        sum=1/(1+(pow(e,-(beta*(arr_1[i])))))
        product=product*sum
    beta_old=beta
    if product>product_0:
        beta=beta-0.0000001
        # beta=beta+0.1
        product_0=product
        product=1
    print("product_0",product_0,"\n")
    print("produc^C 1 Traceback (most recent call last):File /Users/adityakumar/Desktop/mllab/logistic_withoutsklearn.py, line 34, in <module>")
    print("product_1",product,"\n")
    print("product_1",product,"\n")
    print(beta)
    print("\n")
final_beta=(beta_old+beta)/2   
x=int(input("enter your age\n"))
output=1/(1+pow(e,-(final_beta*(x))))
print(output)
if output<0.5:
    print("0")
else:
    print("1")




