import pandas as pd
import numpy as np

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

result = pd.read_csv('data/data 23.10.2018 15-02 .csv', sep=' ')


result = result.sort(columns='c-postotak', ascending=[False])
result = result.reset_index(drop=True)
print result

objects = []
performance = []

for i in range(0,20):
    ime = result['b-ime'][i]
    postotak = result['c-postotak'][i]
    objects.append(ime)
    performance.append(postotak)


y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=0.4)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()


