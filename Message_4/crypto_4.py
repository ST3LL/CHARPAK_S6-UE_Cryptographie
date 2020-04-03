# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:46 2020

@author: tinou
"""


with open('message3.txt', 'r') as file:
    message = file.read() 
#print(message)


def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d


def cle_probable(message):
    carac = frequences(message)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle


def cesar_chiffrage(nb, decalage):
    return (ord(nb) + decalage)
    
def cesar_dechiffrage(nb, decalage):
    return (ord(nb) - decalage)
    

def cesar(message, decalage):
    new_message = []
    m = list(message)
    for l in m:
        crypt = chr(cesar_dechiffrage(l, decalage))
        new_message.append(crypt)
    new = "".join(new_message)
    return new


if __name__ == "__main__":
    print(cesar(message, cle_probable(message)))
    

    
    