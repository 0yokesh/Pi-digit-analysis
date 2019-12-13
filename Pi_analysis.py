#Analysis of Pi digits

import numpy as np
import matplotlib.pyplot as plt
import time

f = open("pi_dec_1m.txt", "r");

data = f.read()

n = len(data)
tracker = np.zeros([10,1], dtype = np.int_)
percent = np.zeros([10,1], dtype = np.float_)
x = np.zeros([10,1], dtype = np.int_)

start_time = time.time()

for i in range(2, n):
    tracker[int(data[i])] += 1
    
print("--- %.8f seconds ---" % (time.time() - start_time))
f.close()
 
for i in range(0, len(tracker)):
    percent[i] = tracker[i]/(n-2)*100;
    x[i] = i
    
#Plotting
plt.plot(x, percent, "k*")
plt.xlabel("#digits")
plt.ylabel("Percentage of occurance")
plt.title("Occurance of #digits in first 1 million digits of Pi")

for a,b in zip(x, percent): 
     plt.text(a, b, str(b))
    
plt.show()
    
    