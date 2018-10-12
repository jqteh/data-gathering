import pandas as pd
import numpy as np

coin =[]

url = 'https://api.coinmarketcap.com/v1/ticker/?limit=200'
df = pd.read_json(url, orient='columns')

print len((df))

df1 = df[['name','symbol']]

print df['name'][1]





 
    
    
    
