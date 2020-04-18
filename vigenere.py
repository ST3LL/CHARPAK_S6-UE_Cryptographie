#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:56:31 2020

@author: tinou_99
"""

with open('nomdufichier.txt', 'r') as file:
    message = file.read() 
print(message)



def mot_plus_long(message):
    mot_long = ""
    msg = message.split()
    for mot in msg:
        if len(mot) > len(mot_long):
            mot_long = mot
    return mot_long, len(mot_long)
        


def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d



def freq_max(msg):
    carac = frequences(msg)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    return carac_max



def d_vigenere_abc(message,cle) :
    l=[]
    for c,lettre in enumerate(message) :
        if lettre in string.ascii_lowercase :
            e = ord(lettre) - ord(cle[c % len(cle)])
            n_lettre = chr(e % 26 + ord('a'))            
        l.append(n_lettre)
    return "".join(l)



def dechiffre_vignere(message, cle):
    l = []
    for c, lettre in enumerate(message):
        e = ord(lettre) - cle[c % len(cle)]
        n_lettre = chr(e % 255)
        l.append(n_lettre)
    return "".join(l)



"""
def cle_probable(n_carac):
    carac = frequences(n_carac)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle
    
    
    
def indice_coincidence(message) :
    freq = frequences(message) 
    s = sum (n*(n-1) for n in freq)
    somme = sum(freq)
    return s / (somme*(somme-1))
"""



if __name__ == "__main__":
    #cle = [-23, -45]
    #cle = [2,9,3]
    #print(dechiffre_vignere(message, cle))
    #print(cle_probable(message))
    #print(freq_max(message))