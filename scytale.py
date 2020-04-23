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
        >>> scytale("mseureeea p ctsgsesr ", 3) == message super secret 
        True
    """
    n_msg = []
    for i in range(cle):
        for j in range(i, len(message), cle):
            n_msg.append(message[j])
    return "".join(n_msg)
    

    
def auto_scytale(message):
    """
    Prend en argument une chaîne de caractères. Renvoie une chaîne de 
    caractères pour laquelle on a appliqué la fonction scytale() à partir d'une
    clé.
        
    Entrée:
        (str)
    Sortie:
        (str) 
    Test:
        >>> auto_scytale("mseureedJlea p cteo sgsesr  ë ") == message super secret de Joël
        True
    """
    for i in range(0, 2000):
        if "Joël" in scytale(message, i):
            return scytale(message, i)



if __name__ == "__main__":
    print(auto_scytale(message))
