import numpy as np
import pandas as pd
#import investpy
import yfinance as yf
from fastai.tabular.all  import *

#data = __file__

def modifyData(ticker):
    
    df = yf.Ticker(ticker).history(period='10y')
   
    
    #Creating another dataset with only close and date
    new_data = pd.DataFrame(index=range(0,len(df)), columns=['Date','Close'])

    for i in range(0, len(df)):
        new_data['Date'][i] = df.index[i]
        new_data['Close'][i] = df['Close'][i]
 
    #create features
    
    new_data = add_datepart(new_data, 'Date')
    new_data.drop('Elapsed', axis=1, inplace=True)


    new_data['mon_fri'] = 0
    for i in range(0, len(new_data)):
        if (new_data.loc[i,'Dayofweek'] == 0 or new_data.loc[i,'Dayofweek']==4):
            new_data.loc[i,'mon_fri'] = 1
        else:
           new_data.loc[i,'mon_fri'] = 0



    #print(new_data.loc[:,['Close','Dayofweek','mon_fri']])



    return new_data

