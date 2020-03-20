#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:13:41 2020

@author: tinou_99
"""

"""
with open('message5.txt', 'r') as file:
    message = file.read() 
#print(message)


def new_freq(m):
    l = [0 for x in range(26)]
    for e  in m:
        i = ord(lettre) - 65
        if 0 <= i > 26:
            l[i] = l[i] + 1
    return (l)
"""


def d_vigenere(message, key):
    m = ""
    i = 0
    for l in message :
        d = ord(l)-65
        nb2 = (d + key[i]) % 26
        i = (i + 1) % len(key)
        m += chr(nb2 + 65)
    return m
 
    
    
if __name__ == "__main__":
    message = "dhkmjcmhvwiilrpzi"
    key = "bachelierbachelie"
    print(d_vigenere(message, key))
    
    
    
    