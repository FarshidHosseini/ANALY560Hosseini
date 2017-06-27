import pandas as pd
import datetime as dt
from datetime import timedelta 
from pandas_datareader import data

company = "VHC"
start = "2010-01-01"
end = dt.datetime.today().strftime("%m/%d/%Y")
# Load data from google finance
company_data = data.DataReader(name = company, data_source = "google", start = start, end = end)
# calculate returns
company_return = company_data.pct_change()
# merege two data frames
stock_data =pd.merge(company_data, company_return, how='left', on=None, left_on=None, right_on=None,
         left_index=True, right_index=True, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
stock_data.columns = ['Open', 'High','Low','Close', 'Vloume', 'Open_return','Hight_return','Low_return','Close_return','Vol_Change']
stock_data.to_csv("stock_data.csv", index = True, encoding = "utf-8")
