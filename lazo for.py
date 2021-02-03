# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:29:09 2021

@author: user
"""
listasw=[]
listart=[]
listantw=[]
lista=["R1" , 'R2' , 'R3'
       , 'S1' , 'S2','S3',
       'R4','R5','PC',
       'Ps5','Ponchadora']
for i in lista:
    if 'S' in i:
        listasw.append(i)
        
    elif "R" in i:
        listart.append(i)
        
    elif"P" in i:
        listantw.append(i)
        
print("lista",lista)
print("sw",listasw)
print("rt",listart)
print("ntw",listantw)