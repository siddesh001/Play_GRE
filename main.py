#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:10:54 2018

@author: siddesh
"""
import random

word_list='words.txt'
def loadwords():
    file=open(word_list,'r')
    line=file.readlines()   
    return(line[random.randint(0,677)])

recent=[]
def add_to_recent(a):
    if a not in recent:
        recent.append(a)

def display(recent):
    print("Recent :")
    print("______________________________________________________________\n")
    for r in range(len(recent)):
        print(recent[r])
    print("______________________________________________________________")


input_c=True
while(input_c):
    
    input_c=input()
    if input_c=='c':
        break
    else:
        input_c=True
    a=loadwords()
    add_to_recent(a)
    a=a.split("-")
    print(a[0],end="")
    #print("Try a sec. & Remembering the meaning..!")
    input()
    print(a[1])
    input()
    display(recent)
    



    
