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



def d_vigenere(message, key):
    m = ""
    i = 0
    for l in message :
        d = ord(l) - 65
        nb2 = (d + key[i])%26
        i = (i + 1) % len(key)
        m += chr(nb2 + 65)
    return m
"""
 
def decalage_g(c, k):
    return chr(ord(c) - ord(k))
 
def decalage_d(c, k):
    return chr(ord(c) + ord(k))
 
#ValueError: chr() arg not in range(0x110000) 
    

def d_vigenere(message, key):
    n_message = list(message)
    k = list(key)
    m = []
    i = 0
    for l in message :
        m.append(decalage_g(l, k[i]))
        n_message = ''.join(m)
        i += 1
    return n_message
     
if __name__ == "__main__":
    message = "dhkmjcmhvwiilrpzi"
    key = "bachelierbachelie"
    print(d_vigenere(message, key))
    
    
    