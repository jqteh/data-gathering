import glob
import pandas as pd

import os
files = os.listdir('C:\Users\mile\Desktop\python\data_4chan\data')
# glob.glob('data*.csv') - returns List[str]
# pd.read_csv(f) - returns pd.DataFrame()
# for f in glob.glob() - returns a List[DataFrames]
# pd.concat() - returns one pd.DataFrame()
df = pd.concat([pd.read_csv(f, sep=' ').set_index('b-names') for f in glob.glob('data*.csv')], ignore_index = True)

print df
