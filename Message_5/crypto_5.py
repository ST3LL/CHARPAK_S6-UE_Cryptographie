#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:13:41 2020

@author: tinou_99
"""

import string

with open('message5.txt', 'r') as file:
    message = file.read() 
#print(message)


#déchiffrage vigenère pour 26 lettres alphabet français 
def d_vigenere_abc(message,key) :
    cypher=[]
    for i,letter in enumerate(message) :
        if letter in string.ascii_lowercase :
            letter = ord(letter) - ord(key[i % len(key)])
            letter = chr(letter % 26 + ord('a'))            
        cypher.append(letter)
    return "".join(cypher)


 
if __name__ == "__main__":
    message = "dhkmjcmhvwiilrpzi"
    key = "bachelierbachelie"
    print(d_vigenere_abc(message, key))
    