# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:27:07 2018

@author: ImBidExter
"""

import sqlite3

conn = sqlite3.connect('drugs.db')

c = conn.cursor()

c.execute("""CREATE TABLE drugs (
            name text PRIMARY KEY,
            cost integer,
            quantity integer
            )""")

conn.commit()

conn.close()