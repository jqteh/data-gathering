import glob
import pandas as pd

path =r'C:\Users\mile\Desktop\python\data_4chan\data' # use your path
allFiles = glob.glob(path + "data*.csv")


for files in allFiles:
    df = pd.read_csv(files ,sep=' ')
    print df
