import re
import string
import pandas as pd

frequency = {}
document_text = open('komentarii 2018.10.11. 20-59.txt', 'r')
text_string = document_text.read()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
frequency_list = sorted(frequency_list)

broj = (len (frequency_list))

url = 'https://api.coinmarketcap.com/v1/ticker/?limit=200'
df = pd.read_json(url, orient='columns')
df1 = df[['name','symbol']]


for i in range (0, len(df1)):
    ime = df['name'][i].lower()
    for j in range (0, len(frequency_list)):
        if (ime == frequency_list[j]):
            a = (frequency[frequency_list[j]])
            b =  broj
            c = (((a*1.0) / b) * 100)
            if ( c >= 0.1):
                print (ime + " ")
                print(str(c) + "%")
                print('\n')
                
                
    
        
    
    
    


"""
    
    print(frequency_list[i])


for words in frequency_list:

if (words == df['name']):
        print words, frequency[words]
        print frequency[words]
        print broj
        print type(frequency[words])
        print type(broj)
        a = (frequency[words])
        b =  broj
        c = (((a*1.0) / b) * 100)
        print(str(c) + "%")    
    
        
        

wordstring = open('procisceni.txt', 'r')
wordstring = wordstring.read()
wordstring = str(wordstring)

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

#print(wordstring)
#print(wordlist)
print(wordfreq)
   
print(len(wordstring))
print(len(wordlist))
print(len(wordfreq))

print(type(wordstring))
print(type(wordlist))
print(type(wordfreq))


file = open('freq.txt','w') 
file = str(file)
file.write(wordfreq) 
 
file.close() 

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))
"""
