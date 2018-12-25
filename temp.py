# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# Print the Pharmacy Bill
p = []
n = []
print ("Enter the Price and the Number of Products Seprated \n Enter '=' for the Bill")
def store():
    a = input("Enter    ")
    if (a=="="):
        if(len(p)==0):
            print("No Product")
        else:
            bill()
    else:
        c =a.split(" ")
        p.append(c[0])
        n.append(c[1])
    store()
    
def bill():
    t = 0
    x = 0
    while x < len(p):
        print(p[x]+" * "+n[x])
        t += (float(p[x])*float(n[x]))
        x+=1
        
    print("Bill = ",t)

store()