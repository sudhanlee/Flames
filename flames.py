#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:39:49 2021

__author__ = 'sudhanlee'
"""


def Flames(name1,name2):
    flames=["Friend","Love","Affection","Marriage","Enemy","Sister"]
    #Removing the comman letters in the name
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i] == name2[j]:
                name1[i] = name2[j] = ""

    #converting the name2 to string
    name1 = "".join(name1)
    name2 = "".join(name2)
    
    #Total length of the names
    length = len(name1) + len(name2)
    
    #Main logic of flames (The counting part!!!)
    while len(flames) != 1:
        
        val = (length%len(flames))-1
        
        flames = flames[val:] + flames[:val]
        flames.pop(0)
    
    return flames[0]

#Main Screen

while True:
    print("1.Check FLames")
    print("2.Exit")
    choice  = int(input("Enter your choice : "))
    if choice ==1:
        name1 = list(input("Enter First name : "))
        name2 = list(input("Enter Second name 2: "))
        x = Flames(name1, name2)
        print("\r\n",x,"\r\n")
    elif choice == 2:
        print("Thanks for executing !!!")
        break
    else:
        print("\r\n Invaid Input \r\n")
