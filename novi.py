import glob
import pandas as pd


path =r'C:\Users\mile\Desktop\python\data_4chan\data\data' # use your path

df = pd.concat([pd.read_csv(f, sep =' ', usecols=[1,3]).set_index('b-ime') for f in glob.glob(path + '*.csv')], axis=1)    
    

