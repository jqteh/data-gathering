import glob
import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt

path =r'C:\Users\mile\Desktop\python\data_4chan\data\data' # use your path

df = pd.concat([pd.read_csv(f, sep =' ', usecols=[1,3]).set_index('b-ime') for f in glob.glob(path + '*.csv')], axis=1)    

#path1 =r'C:\Users\mile\Desktop\python\data_4chan\data_cmc' # use your path

df1 = pd.concat([pd.read_csv(f, sep =' ', usecols=[1,4]).set_index('name') for f in glob.glob('*.csv')], axis=1)    

#yolo = glob.glob('data*.csv')
"""
f = df.loc['ada']
p = df.loc['ark']
r = df.loc['bitcoin']
s = df.loc['chainlink']
x = df.loc['doge']
u = df.loc['civic']
"""
t = range(0,87)

#y1 = f
#y2 = p

plt.subplot(2, 1, 1)
f = df.loc['chainlink']
#f = sigmoid(f)
f.plot()
plt.title('usporedba freq i cijene')
plt.ylabel('freq')
plt.show()

plt.subplot(2, 1, 2)
p = df1.loc['Chainlink']
#p = sigmoid(p)
p.plot()
plt.xlabel('dolars')
plt.ylabel('price')

price = p[:50]

"""
ada
aion
amb
arb
ark
bitcoin
chainlink
cindicator
civic
dai
dash
decentraland
doge
eng
eos
eth
ethlend
ethos
"""