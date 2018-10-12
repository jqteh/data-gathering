import pandas as pd
from bs4 import BeautifulSoup
import re
import string
import time
import datetime

for i in range (0, 20):
	now = time.strftime("%Y.%m.%d. %H-%M")
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

	print("\nreading " + str(len(df1)) + " threads.  \n" )

	for i in range (0, len(df1)):    
		#uzimam id i dodajem u url
		broj = str(df1.no[i])   
		thread_url = "https://a.4cdn.org/biz/thread/" + broj + ".json" 
		#uzimanje podataka od threada
		df2 = pd.read_json(thread_url, orient='columns')
		for j in range (0, len(df2)):
			data1 = df2.posts[j]
			sadrzaj.append(data1)

	#pristupanje pojedinom komentaru 
	for i in range (0, len(sadrzaj)):
			data2 = sadrzaj[i]
			komentari_svi.append(data2)
	   
	#pretvaranje u data frame
	df2 = pd.DataFrame.from_dict(sadrzaj)
	df2.to_csv('komentari.csv', sep=' ', encoding='utf-8')

	print("reading time %s seconds " % (time.time() - start_time))
	print("\nnumber of com " + str(len(komentari_svi)))

	#----------------------clearing data---------------------------------------------------

	df = pd.read_csv('komentari.csv', delimiter=' ')

	for i in range (0, len(df)):
		data = df.com[i]
		komentari.append(data)

	for i in range (0, len(komentari)):
		data = komentari[i]
		sadrzaj.append(data)

	sadrzaj = str(sadrzaj)
	"""
	sadrzaj = '\n'.join(komentari)
	print(sadrzaj)
	"""
	#convert from html to text
	cleantext = BeautifulSoup(sadrzaj).text
	#removing id of replies
	final = re.sub(">>\d+", "", cleantext)
	final = re.sub("\d\d\d\d\d+", "", cleantext)
	final = re.sub(">", "", final)
	final = re.sub(r'[^\w\s]',' ',final)
	final = re.sub(" {2,}",' ',final)
	final = final.lower()
	print(type(final))
	print("komentari procisceni")

	file = open('komentarii %s.txt' % now, 'w')
	file.write(final.encode('utf-8'))
	file.close()

	print('procisceni komentari uspijesno pohranjeni u .txt :)')
	print(len(final))
	print("--- %s seconds ---" % (time.time() - start_time))
	time.sleep(60*10)

print('komentari preuzeti')



