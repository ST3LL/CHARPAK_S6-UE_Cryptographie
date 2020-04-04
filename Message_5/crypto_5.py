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
def d_vigenere_abc(message,cle) :
    c=[]
    for i,lettre in enumerate(message) :
        if lettre in string.ascii_lowercase :
            lettre = ord(lettre) - ord(cle[i % len(cle)])
            lettre = chr(lettre % 26 + ord('a'))            
        c.append(lettre)
    return "".join(c)



def d_vigenere(message, cle) :
    n_msg = []
    n_cle = [ord(e) for e in cle]
    msg = [ord(k) for k in message]
    for i in range(len(msg)) :
        msg[i] -= int(n_cle[i % len(n_cle)])
        print(msg[i])
        n_msg.append(chr(msg[i]))        
    return "".join(n_msg)


 
if __name__ == "__main__":
    message = "dhkmjcmhvwiilrpzi"
    cle = "bachelierbachelie"
    #print(d_vigenere_abc(message, key))
    print(d_vigenere(message,cle))
