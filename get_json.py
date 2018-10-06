# -*- coding: cp1250 -*-
import pandas as pd
import numpy as np
from django.utils.encoding import smart_str, smart_unicode

sve = []
svi_postovi = []
sadrzaj = []
komentari= []

# Create URL to JSON file (alternatively this can be a filepath)
url = 'http://a.4cdn.org/biz/threads.json'
# Load the first sheet of the JSON file into a data frame
df = pd.read_json(url, orient='columns')

#ucitavanje threadova sa stranica od 0 do 11
for i in range (0, 11):   
    data = df.threads[i]  
    rez = pd.DataFrame.from_dict(data)    
    sve.append(rez)
#tablica formata index, last_modified, no
all_nos = pd.concat(sve, ignore_index=True)
df1 = pd.DataFrame.from_dict(all_nos)

print(type(sve))
print(type(all_nos))
print(type(df1))


print("\n OBRADA SADRZAJA " + str(len(df1)) + " threadova  \n" )

for i in range (0, len(df1)):    
    #uzimam id i dodajem u url
    broj = str(df1.no[i])   
    thread_url = "https://a.4cdn.org/biz/thread/" + broj + ".json" 
    #uzimanje podataka od threada
    print("thread > " + str(i) + ", ID threada > " + broj )
    df2 = pd.read_json(thread_url, orient='columns')
    for j in range (0, len(df2)):
        data1 = df2.posts[j]
        sadrzaj.append(data1)
        
    
    print("broj komentara > " + str(len(data1)) + "\n")
    



print("\n sadrzaj obraden \n")
#info
print("\n TIP > " + str(type(sadrzaj)) +  "\n")
print("\n broj stupaca > " + str(len(sadrzaj[0])) +  "\n")
print("\n broj redaka > " + str(len(sadrzaj)) +  "\n")

#pristupanje pojedinom komentaru
for i in range (0, len(sadrzaj)):
        data2 = sadrzaj[i]
        komentari.append(data2)
        
print("\n komentari obradeni- \n")
print("\n ukupni broj KOMENTARA -> " + str(len(komentari)) +  "\n")
print("\n  komentari obradeni \n")
print("\n PRETVARANJE U DATA FRAME \n")
"""
    no - integer 	Post number 	1-9999999999999
    now - string 	Date and time 	MM/DD/YY(Day)HH:MM (:SS on some boards), EST/EDT timezone
    sub - string 	Subject 	text
    com - string 	Comment 	text (includes escaped HTML)
    ID - string 	ID 	text (8 characters), Mod, Admin, Manager, Developer, Founder
    replies
    unique_ips
"""
df2 = pd.DataFrame.from_dict(sadrzaj)
print("\n tip sadrzaja i data framea \n")
print(type(sadrzaj))
print(type(df2))
print(len(df2))

comm =(df2['com'])
print("\n uspjesno pretvoreno u data frame")

print("tip podataka" + str(type(comm)))
     
comm.to_csv('komentari.csv', sep='\n', encoding='utf-8')
"""
with open('komentari.txt', 'w') as f:
    for item in comm:
        f.write(str(item))
f.close()
"""
print("\n pohranjeno u datoteku \n")

  


