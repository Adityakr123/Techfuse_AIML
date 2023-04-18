import pandas as pd
from sklearn import linear_model
from sklearn.metrics import accuracy_score
df = pd.read_csv("multiple_regression.csv")
print(df)
X=df[['Age(years)','Mileage(K miles)']]
Y=df['Price(kg)']
regr = linear_model.LinearRegression()

regr.fit(X,Y)
# print('Intercept:\n', regr.intercept_)
# print('Coefficients:\n', regr.coef_)
x1=float(input("Enter Age"))
x2=float(input("Enter Milage"))
print('Predicted Price:\n',regr.predict([[x1,x2]]))