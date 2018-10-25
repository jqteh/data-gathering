import time

import pandas as pd
import numpy as np

from nltk.corpus import stopwords
import re
import string

from bs4 import BeautifulSoup
import json
import urllib
for i in range(0, 60):
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
        for i in range (2, len(df1)):
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

                     
        df2 = pd.DataFrame.from_dict(sadrzaj)

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

        file = open('komentari/komentari %s.txt' % now , 'w')
        file.write(final.encode('utf-8'))
        file.close()

        print('\nprocisceni komentari uspijesno pohranjeni u .txt :)\n')
        print("--- %s seconds ---\n" % (time.time() - start_time))

        #----------racunanje frekvencija ----------

        frequency = {}
        document_text = open('komentari/komentari %s.txt' % now , 'r')

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

        rankovi = []
        imena = []
        postotci = []
        for i in range(1, len(df)):
            
            if df['b-names'][i] == df['b-names'][i-1]:
                rank = df['a-rank'][i]
                ime = df['b-names'][i]
                postotak = df['c-percents'][i]
                rankovi.append(rank)
                imena.append(ime)
                postotci.append(postotak)

          
        df1 = pd.DataFrame(
            {
                "a-rank": rankovi,
                "b-ime": imena,
                now: postotci
            }
        )

        rankovi = []
        imena = []
        postotci = []
        for i in range(1, len(df)):
            
            if df['b-names'][i] != df['b-names'][i-1] and df['a-rank'][i] == df['a-rank'][i-1] :
                rank = df['a-rank'][i]
                ime = df['b-names'][i-1]
                a = float(df['c-percents'][i])
                b = float(df['c-percents'][i-1])
                c = a+b

                rankovi.append(rank)
                imena.append(ime)
                postotci.append(c)
                
        df2 = pd.DataFrame(
            {
                "a-rank": rankovi,
                "b-ime": imena,
                now: postotci
            }
        )

        frames = [df1, df2]

        result = pd.concat(frames,ignore_index=True)
        result = result.reset_index(drop=True)

        result.to_csv('data/data %s .csv' %now, sep=' ', encoding='utf-8')
        
        url = 'https://api.coinmarketcap.com/v1/ticker/?limit=200'
        df = pd.read_json(url, orient='columns')
        df1 = df[['name','symbol', 'rank', 'price_usd', 'price_btc', 'market_cap_usd']]

        df1.to_csv('data_cmc/data %s .csv' %now, sep=' ', encoding='utf-8')

        print "sve uspjesno odradeno i pohranjeno u datoteku"
        print "komentari pohranjeni u komentari folder"
        print "statistike o coinima pohreanjene u folder data"
        print "podatke o coinima pohranjene u data_cmc"
        time.sleep(1*60*10)


