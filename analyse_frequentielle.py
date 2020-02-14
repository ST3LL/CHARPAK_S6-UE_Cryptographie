# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:58:22 2020

@author: tinou
"""

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