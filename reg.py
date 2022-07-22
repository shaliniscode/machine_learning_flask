import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from data import *
from sklearn.linear_model import LinearRegression

#ticker = 'AAPL'

#df = modifyData(ticker)

def model(df):


    df['returns'] = df['Close'].pct_change()
    df_x = df.drop(['Close', 'returns'], axis = 1)
    
    x = df_x.drop(index= df_x.index[0], axis = 0)
    x = x.iloc[:,0:5]

    df_y = df.loc[:,'returns']
    y = df_y.dropna()

    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    #print (X_test)
    preds = model.predict(X_test)

    #print(preds)

    rms = mean_squared_error(y_test, preds)
    score = r2_score(y_test, preds)

    return rms, score

#print(model(df))
