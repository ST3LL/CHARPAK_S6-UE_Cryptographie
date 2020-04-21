#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:56:31 2020

@author: tinou_99
"""

with open('nomdufichier.txt', 'r') as file:
    message = file.read() 



def mot_plus_long(message):
    """
    Prend en argument une chaîne de caractères représentant un message. 
    Renvoie un tuples constitué du mot le plus long du message et de la 
    longueur du mot le plus long.
        
    Entrée:
        (str)
    Sortie:
        (str, int) 
    Test:
        >>> mot_plus_long("message super secret ahah") == ("message", 7) 
        True
    """
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



def d_vigenere_abc(message,cle) :
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



def dechiffre_vignere(message, cle):
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
    #cle = [2,9,3]
    #print(dechiffre_vignere(message, cle))
    #print(cle_probable(message))
    #print(freq_max(message))