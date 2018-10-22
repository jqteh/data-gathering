import re
import string
import time
import pandas as pd
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import json
import urllib

now = time.strftime("%d.%m.%Y %H-%M")
start_time = time.time()

sve = []
sadrzaj = []
komentari_svi= []

komentari = []
table = string.maketrans("","")

url = 'http://a.4cdn.org/biz/threads.json'
df = pd.read_json(url, orient='columns')
	
#ucitavanje threadova 
for i in range (0, len(df)):   
	data = df.threads[i]  
	rez = pd.DataFrame.from_dict(data)    
	sve.append(rez)
	
all_nos = pd.concat(sve, ignore_index=True)
df1 = pd.DataFrame.from_dict(all_nos)

print("\nreading " + str(len(df1)) + " threads....  \n" )

#ide od 1 a ne od 0 jer je prvi thread sa pravilima
for i in range (1, len(df1)):
    broj = str(df1.no[i])
    thread_url = "https://a.4cdn.org/biz/thread/" + broj + ".json"
    
    json_url = urllib.urlopen(thread_url)
    data = json.loads(json_url.read())
    #print type(data)
    print i
    for post in data["posts"]:
            if 'com' in post:
                    data1 = post["com"]
                    sadrzaj.append(data1)

             

#print type(sadrzaj)
#all_com = pd.concat(sadrzaj, ignore_index=True)
df2 = pd.DataFrame.from_dict(sadrzaj)
#print len(df2)
#print sadrzaj[2]
#print df2

df2.to_csv('komentari.csv', sep=' ', encoding='utf-8')
print("\nnumber of com: " + str(len(sadrzaj)))
print("--- %s seconds ---\n" % (time.time() - start_time))


#---------------------- clearing data ----------------------
for i in range (0, len(df2)):
	data = df2[0][i]
	komentari.append(data)

for i in range (0, len(komentari)):
	data = komentari[i]
	sadrzaj.append(data)

sadrzaj = str(sadrzaj)
#convert from html to text
cleantext = BeautifulSoup(sadrzaj).text
#removing id of replies
final = re.sub(">>\d+", "", cleantext)
final = re.sub("\d\d\d\d\d+", "", final)
final = re.sub("\d\d\d\d\d+", "", final)
final = re.sub(">", "", final)
final = re.sub(r'[^\w\s]',' ',final)
final = re.sub(" {2,}",' ',final)
final = final.lower()

file = open('komentari/komentari%s.txt' % now , 'w')
file.write(final.encode('utf-8'))
file.close()

print('\nprocisceni komentari uspijesno pohranjeni u .txt :)\n')
print("--- %s seconds ---\n" % (time.time() - start_time))

#----------racunanje frekvencija ----------

frequency = {}
document_text = open('komentari/komentari%s.txt' % now , 'r')

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

print "broj rijeci " + str(broj) + "\n"

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
df.to_csv('data/data %s .csv' %now, sep=' ', encoding='utf-8')

print "sve uspjesno odradeno i pohranjeno u datoteku KRV TI JEBEM"
print "komentari pohranjeni u komentari folder"
print "statistike o coinima pohreanjene u folder data"


