#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:22:33 2020

@author: tinou_99
"""

with open('nomdefichier.txt', 'r') as file:
    message = file.read() 
    
    

def scytale(message, cle):
    """
    Prend en argument une chaîne de caractères et et un entier représentant
    la clé et renvoie une chaîne de caractères correspond au déchiffrage du 
    message en appliquant la méthode dite de la scytale.
        
    Entrée:
        (str, int)
    Sortie:
        (str) 
    Test:
        >>> scytale("mgpeeeecs rrss eaust", 3) == message super secret 
        True
    """
    n_msg = []
    for i in range(cle):
        for j in range(i, len(message), cle):
            n_msg.append(message[j])
    return "".join(n_msg)
    

    
if __name__ == "__main__":
    #cle = 
    print(scytale(message, cle))