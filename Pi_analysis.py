#Analysis of Pi digits

#Created by Yokesh
#Email: yzs0074@auburn.edu

import numpy as np
import matplotlib.pyplot as plt
import time

#Input the .txt file from the link in the description
f = open("pi_dec_1m.txt", "r");

#Read the entire .txt file as a string
#Beware you should have enough to memory to handle, when to try >1e9 digits
data = f.read()

#Initialize
n = len(data)
tracker = np.zeros([10,1], dtype = np.int_)   #Tracks the count of each #digit
percent = np.zeros([10,1], dtype = np.float_) # To find percent of each #digit
x = np.zeros([10,1], dtype = np.int_)         # Variable to plot (optional)

start_time = time.time()   #Keep track of time (optional)

#Remember the loop runs from third character to eliminate 3. at the start
for i in range(2, n):
    tracker[int(data[i])] += 1
    
print("--- %.8f seconds ---" % (time.time() - start_time))  #Prints the time elapsed (optional)
f.close()
 
#Loop to calculate the percent of each #digit
for i in range(0, len(tracker)):
    percent[i] = tracker[i]/(n-2)*100;
    x[i] = i
    
#Plotting
plt.plot(x, percent, "k*")
plt.xlabel("#digits")
plt.ylabel("Percentage of occurance")
plt.title("Occurance of #digits in first 1 million digits of Pi")

#To display the values of each data point
#This section yet to updated with beautiful looking data points and x-axis labels
for a,b in zip(x, percent): 
     plt.text(a, b, str(b))
    
plt.show()
    
    
