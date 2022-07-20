import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.model_selection import KFold, cross_val_predict
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
#from sklearn.pipeline import Pipeline
from data import data
sns.set()





#print(data['Close'].head())
#spliting the data
X_train, X_test, y_train, y_test = train_test_split(data['Close'], test_size=0.3,random_state=42)



alphas = [0.005, 0.05, 0.1, 0.3, 1,3, 5, 10, 15, 30, 80]

lassoCV = LassoCV(alphas=alphas, cv=4).fit(X_train, y_train)

lassoCV_rmse = mean_squared_error(y_test, lassoCV.predict(X_test))

print("The best alpha is {} with Root Mean square Error:{}".format(lassoCV.alpha_, lassoCV_rmse))

LASSO_r2 = r2_score(y_test, lassoCV.predict(X_test))
print("Rsquare:", LASSO_r2)