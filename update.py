# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:51:53 2018

@author: ImBidExter
"""

import sqlite3

conn = sqlite3.connect('drugs.db')

c = conn.cursor()

n = input("Enter the Name of the Product       ")
p = input("Enter the New Price of the Product       ")
q = input("Enter the New Arrival Quantity of the Product       ")


c.execute("UPDATE drugs SET cost=? WHERE name=?", (p, n))

c.execute("UPDATE drugs SET quantity=? WHERE name=?", (q, n))

conn.commit()

conn.close()