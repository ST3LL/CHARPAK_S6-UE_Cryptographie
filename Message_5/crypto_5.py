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





def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d



def cle_probable(n_carac):
    carac = frequences(n_carac)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle



def cesar_dechiffrage(lettre, cle):
    return (ord(lettre) - cle)
    
    

def cesar(message, cle):
    new_message = []
    m = list(message)
    for l in m:
        crypt = chr(cesar_dechiffrage(l, cle))
        new_message.append(crypt)
    new = "".join(new_message)
    return new


def separateur(message, l_cle):
    sep = []
    for c in range(l_cle):
        sous_sep = []
        for e in range(c, len(message), l_cle): #pas de longueur de la clé
            sous_sep.append(message[e])
        sep.append(sous_sep)
    return sep



def colleur(v_msg):
    n_msg = []
    for c in range(len(v_msg)):
        for e in range(len(v_msg[c])):
            try : 
                n_msg.append(v_msg[e][c])
            except : 
                pass
    return ''.join(n_msg)



def d_vigenere(message, l_cle):
    n_msg = []
    sep = separateur(message, l_cle) 
    for c in sep :
        cle = cle_probable()
        n_msg.append(cesar(c, cle))
    return colleur(n_msg)




"""
def d_vigenere(message, cle) :
    n_msg = []
    n_cle = [ord(e) for e in cle]
    msg = [ord(k) for k in message]
    for i in message :
        msg[i] -= int(n_cle[i % len(n_cle)])
        #print(msg[i])
        n_msg.append(chr(msg[i]))  
        sup = cle_probable(message)
        n_msg = cesar(message, sup)    
    return "".join(n_msg)
"""


 
if __name__ == "__main__":
    message = "dhkmjcmhvwiilrpzi"
    l_cle = 3
    #print(d_vigenere_abc(message, key))
    print(d_vigenere(message,l_cle))
