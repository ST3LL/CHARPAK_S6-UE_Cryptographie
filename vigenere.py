#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:56:31 2020

@author: tinou_99
"""

import string

with open('nomdufichier.txt', 'r') as file:
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



def d_vigenere_abc(message, cle) :
    """
    Prend en argument une chaîne de caractères représentant un message et une 
    chaîne de caractère représentant la clé. Renvoie une chaîne de caractères 
    correspond au déchiffrage du message en appliquant la méthode dite de 
    vigenère (seulement pour les 26 lettres de l'alphabet français).
        
    Entrée:
        (str, str)
    Sortie:
        (str) 
    Test:
        >>> d_vigenere_abc("ovqhtug jsexf uvagxh", "crypto") == message super secret 
        True
    """
    l=[]
    for c,lettre in enumerate(message) :
        if lettre in string.ascii_lowercase :
            e = ord(lettre) - ord(cle[c % len(cle)])
            n_lettre = chr(e % 26 + ord('a'))            
        l.append(n_lettre)
    return "".join(l)



def dechiffre_vigenere(message, cle):
    """
    Prend en argument une chaîne de caractères représentant un message et 
    entier la clé. Renvoie une chaîne de caractères correspond au déchiffrage 
    du message en appliquant la méthode dite de vigenère.
        
    Entrée:
        (str, int)
    Sortie:
        (str) 
    Test:
        >>> dechiffre_vigenere("ow zcy'ult2 le{", [2, 18, 45, 7]) == message super secret 
        True
    """
    l = []
    for c, lettre in enumerate(message):
        e = ord(lettre) + cle[c % len(cle)]
        n_lettre = chr(e % 255)
        l.append(n_lettre)
    return "".join(l)



if __name__ == "__main__":
    cle = [2,9,3]
    print(dechiffre_vigenere(message, cle))  