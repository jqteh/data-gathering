import time

start_time = time.time()

file = open('komentarii 2018.10.11. 20-59.txt', 'r')

from collections import Counter
wordcount = Counter(file.read().split())

print(len(wordcount))

print("--- %s seconds ---" % (time.time() - start_time))


