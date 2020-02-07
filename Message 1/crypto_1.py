# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:22:57 2020

@author: tinou_99
"""

import numpy as np


with open('message1.txt', 'r') as file:
    message = file.read() 
    
    

def frequences(texte):
    """
    Prend en argument une chaîne de caractères et renvoie un dictionnaire 
    dont les clés sont les caractères présents dans le texte et les valeurs 
    sont le nombre d'occurences du caractère concerné.
        
    Entrée:
        (str) 
    Sortie:
        (dict()) 
    Test:
        >>> frequences('bonjour') == {'b': 1, 'j': 1, 'n': 1, 'o': 2, 'r': 1, 'u': 1}
        True
        >>> frequences('ABRACADABRA') == {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2}
        True
    """
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d



def decrypt(texte, nb):
    tab = [texte[k: k + nb] for k in range(0,len(texte)+1,nb+1)]
    
    return tab
    
    
    

if __name__ == "__main__":
    """
    for e in reversed(sorted(frequences(message).items(), key=lambda t: t[1])):
        print(e)
    """
    for cle in range(1,1000):
        print("".join([l[0] for l in decrypt(message, cle) if len(l) != 0]))
        #print("".join(l[0] for l in oui))
    
    
        
        