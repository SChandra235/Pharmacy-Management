# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:37:26 2018

@author: ImBidExter
"""

import csv
import matplotlib.pyplot as plt
p=[]
q=[]
with open('drugs.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print(data)
for f in range(len(data)):
    p.append(data[f][1])
    q.append(data[f][2])
    
del q[0]
del p[0]
print(q)
print(p)
#emp_ages = [22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19]
bins1 = [0,1,2,3,4,5,6]
plt.hist(p, bins1, histtype='bar', rwidth = 0.5, color = 'blue')
plt.xlabel('Price')
plt.ylabel('No. of Drugs')
plt.title('Pharmacy Store')
plt.show()


bins2 = [0,1,2,3,4,5,6]
plt.hist(q, bins2, histtype='bar', rwidth = 0.5, color = 'red')
plt.xlabel('Qunatity')
plt.ylabel('No. of Drugs')
plt.title('Pharmacy Store')
plt.show()