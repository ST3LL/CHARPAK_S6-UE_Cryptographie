#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:50:47 2020

@author: tinou_99
"""

import matplotlib.pyplot as plt



with open('message6.txt', 'r') as file:
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
        try:
            crypt = chr(cesar_dechiffrage(l, cle))
        except:
            crypt = "#"
        new_message.append(crypt)
    new = "".join(new_message)
    return new



def separateur(message, l_cle):
    return [message[c: len(message): l_cle] for c in range(l_cle)]
    


def liste_plus_grand(l_liste):
    return max(map(len, l_liste))



def colleur(v_msg):
    n_msg = []
    taille_max = liste_plus_grand(v_msg)
    for c in range(taille_max):
        for e in range(len(v_msg)):
            try : 
                n_msg.append(v_msg[e][c])
            except : 
                pass
    return ''.join(n_msg)



def auto_cesar(message):
    return cesar(message, cle_probable(message))



def auto_vigenere(message, l_cle):
    sep = separateur(message, l_cle)
    l = [auto_cesar(e) for e in sep]
    return colleur(l)



def mot_plus_long(message):
    return max(map(len,message.split(' ')))


 
if __name__ == "__main__":
    #plt.plot([mot_plus_long(auto_vigenere(message, i)) for i in range(1,10)]) #probabilité d'avoir une longueur de clé de ...+1
    #plt.show()
    
    l_cle = 6
    print(auto_vigenere(message,l_cle))