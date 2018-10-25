import re
import string
import pandas as pd
from nltk.corpus import stopwords

frequency = {}
document_text = open('procisceni/komentari14.10.2018 14-37.txt', 'r')

en_stops = set(stopwords.words('english'))
all_words = document_text

text_string = document_text.read()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
frequency_list = sorted(frequency_list)

broj = (len (frequency_list))

#get coin name and symbol from cmc
url = 'https://api.coinmarketcap.com/v1/ticker/?limit=200'
df = pd.read_json(url, orient='columns')
df1 = df[['name','symbol']]

ranks = []
names = []
percents = []

for i in range (0, len(df1)):
    ime = df['name'][i].lower()
    simbol = df['symbol'][i].lower()
    rank = i+1
    
    for j in range (0, len(frequency_list)):  
        if ime == frequency_list[j]:
            a = (frequency[frequency_list[j]])
            b =  broj
            c = (((a*1.0) / b) * 100)
            c = '%.2f' % c
            ranks.append(rank)
            names.append(ime)
            percents.append(c)
                
        if simbol == frequency_list[j]:
            a = (frequency[frequency_list[j]])
            b =  broj
            c = (((a*1.0) / b) * 100)
            c = '%.2f' % c
            ranks.append(rank)
            names.append(simbol)
            percents.append(c)

df = pd.DataFrame({'a-rank':ranks, 'b-names':names, 'c-percents':percents})
broj = len(df)+1
for i in range (0, broj):
    if (df['a-rank'][i] == df['a-rank'][i+1]):
        print  df['b-names'][i]
    else:
        print " nisu isti" 
"""    
    print df['a-rank'][i]
    print df['a-rank'][i+1]


    if (df['a-rank'][i] == df['a-rank'][i+1] and df['b-names'][i] == df['b-names'][i+1]):
        zajednicki_postotak = df['c-percents'][i] + df['c-percents'][i+1]
        print df['b-names'][i] + zajednicki_postotak
"""       
#df['b-names'][i]
#df['c-percents'][i]
#print df['b-names'][0]




