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
    for i in enumerate(message):
        carac = frequences(message)
        pcarac_max = (max([(carac[e], e) for e in carac], key= lambda x : x[0]) if i % 2 == 0)
        cle_pair = ord(pcarac_max[1]) - ord(' ') 
        icarac_max = max([(icarac[e], e) for e in icarac], key= lambda x : x[0])
        cle_impair = ord(icarac_max[1]) - ord(' ') 
    return cle_pair, cle_impair


def cesar_chiffrage(nb, decalage):
    return (ord(nb) + decalage)
    
def cesar_dechiffrage(nb, decalage):
    return (ord(nb) - decalage)
    

def cesar(message, cle_pair, cle_impair):
    new_message = []
    cle_pair = cle_probable[0]
    cle_impair = cle_probable[1]
    for i, l in enumerate(message):
        crypt = chr(cesar_dechiffrage(l, cle_pair if i % 2 == 0 else cle_impair))
        new_message.append(crypt)
    new = "".join(new_message)
    return new


if __name__ == "__main__":
    print(cesar(message, cle_probable(message)))
    

    
    