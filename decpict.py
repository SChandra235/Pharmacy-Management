# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:33:17 2018

@author: ImBidExter
"""

import matplotlib.pyplot as plt
emp_ages = [22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19]
bins = [0,10,20,30,40,50,60]
plt.hist(emp_ages, bins, histtype='bar', rwidth = 0.8, color = 'green')
plt.xlabel('Employee Ages')
plt.ylabel('No. of Employees')
plt.title('PU')
plt.show()
