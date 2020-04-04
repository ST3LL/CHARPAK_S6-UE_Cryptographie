#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:06:27 2020

@author: tinou_99
"""



with open('nomdufichier.txt', 'r') as file:
    message = file.read() 
print(message)
    


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



def cle_probable(message):
    """
    Prend en argument une chaîne de caractères et renvoie la clé probable 
    pour décrypter un massage à l'aide du code césar.
        
    Entrée:
        (str) 
    Sortie:
        (int) 
    Test:
        >>> cle_probable() == 
        True
    """
    carac = frequences(message)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle



def cesar_chiffrage(lettre, cle):
    """
    Prend en argument une lettre et la clé du code césar et renvoie 
    le décalage (chiffrage d'un message).
        
    Entrée:
        (str, int) 
    Sortie:
        (int) 
    Test:
        >>> cesar_chiffrage("a", 9) == 106
        True
    """
    return (ord(lettre) + cle)
    


def cesar_dechiffrage(lettre, cle):
    """
    Prend en argument une lettre et la clé du code césar et renvoie 
    le décalage (déchiffrage d'un message).
        
    Entrée:
        (str, int) 
    Sortie:
        (int) 
    Test:
        >>> cesar_dechiffrage("a", 9) == 88
        True
    """
    return (ord(lettre) - cle)
    


def cesar(message, cle):
    """
    Prend en argument un message et la clé du code césar et renvoie 
    le message déchiffré.
        
    Entrée:
        (str, int) 
    Sortie:
        (str)
    Test:
        >>> message = "Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm({mkwvl(um{{iom6"
        >>> cesar(message, -8) == "Bravo ! Vous avez déchiffré le second message."
        True
    """
    new_message = []
    m = list(message)
    for l in m:
        crypt = chr(cesar_dechiffrage(l, cle))
        new_message.append(crypt)
    new = "".join(new_message)
    return new




if __name__ == "__main__":
    print(cesar(message , cle_probable(message)))
    
    
    