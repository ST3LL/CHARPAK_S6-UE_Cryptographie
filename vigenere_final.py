#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:33:52 2020

@author: tinou_99
"""

import matplotlib.pyplot as plt



with open('message6.txt', 'r') as file:
    message = file.read() 
#print(message)



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



def mot_plus_long(message):
    """
    Prend en argument une chaîne de caractères et renvoie un entier 
    correspondant au nombre de caractères du mot le plus long du message.
    
    Entrée :
        (str)
    Sortie :
        (int)
    Test :
        >>> mot_plus_long("un mot tel que anticonstitutionnellement") == 25
        True
    """
    return max(map(len,message.split(' ')))



def liste_plus_grand(l_liste):
    """
    Prend en argument une liste de sous-listes et renvoie un entier correspondant au 
    nombre d'éléments de la sous-liste la plus longue de la liste.
    
    Entrée :
        (list)
    Sortie :
        (int)
    Test :
        >>> liste_plus_grand([[1,2,3,4], [1,2,3,4,5,6], [1,2,3,4,5,6,7,8,9,10]]) == 10
        True
    """
    return max(map(len, l_liste))



def cle_probable(n_carac):
    """
    Prend en argument une chaîne de caractères et renvoie la clé probable 
    pour décrypter un massage à l'aide du code césar.
        
    Entrée:
        (str) 
    Sortie:
        (int) 
    Test:
        >>> cle_probable("Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm(um{{iom6") == -8
        True
    """
    carac = frequences(n_carac)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle



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
        >>> message = "Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm(um{{iom6"
        >>> cesar(message, -8) == Bravo ! Vous avez déchiffré le message.
        True
    """
    new_message = []
    m = list(message)
    for l in m:
        try: #pour éviter des erreurs
            crypt = chr(cesar_dechiffrage(l, cle))
        except:
            crypt = "#"
        new_message.append(crypt)
    new = "".join(new_message)
    return new



def separateur(message, l_cle):
    """
    Prend en argument une chaîne de caractères et un entier correspondant
    à la longueur de la clé. Retourne une liste correspondant à la séparation 
    des caractères du message tous les l_cle (longueur de clé).
        
    Entrée:
        (str, int) 
    Sortie:
        (list)
    Test:
        >>> separateur("ouioui se balade dans le parc", 3) == ['oo  lea  r', 'uusba nlpc', 'iieaddsea']
        True
    """
    return [message[c: len(message): l_cle] for c in range(l_cle)]
    


def colleur(v_msg):
    """
    Prend en argument une liste. Retourne une chaîne de caractères, réalisant 
    l'inverse de la fonction separateur().
    
    Entrée:
        (list) 
    Sortie:
        (str)
    Test:
        >>> colleur(['oo  lea  r', 'uusba nlpc', 'iieaddsea']) == ouioui se balade dans le parc
        True
    """
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
    """
    Prend en argument une chaîne de caractères et y applique la méthode césar. 
    Retourne une chaîne de caractères.
    
    Entrée:
        (str) 
    Sortie:
        (str)
    Test:
        >>> message = "Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm(um{{iom6"
        >>> auto_cesar(message) == Bravo ! Vous avez déchiffré le message.
        True
    """
    return cesar(message, cle_probable(message))



def auto_vigenere(message, l_cle):
    """
    Prend en argument une chaîne de caractères et un entier correspondant à la
    longueur de la clé. Retourne une chaîne de caractères pour laquelle la 
    fonction auto_cesar() a été appliquée pour tous les caractères du message 
    initial .
    
    Entrée:
        (str, int) 
    Sortie:
        (str)
    Test:
        >>> message = "Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm(um{{iom6"
        >>> auto_vigenere(message, ) == Bravo ! Vous avez déchiffré le message.
        True
    """
    sep = separateur(message, l_cle)
    l = [auto_cesar(e) for e in sep]
    return colleur(l)


 
if __name__ == "__main__":
    #graph des probabilités d'avoir une longueur de clé de ...+1 en fonction de la longueur des mots
    plt.plot([mot_plus_long(auto_vigenere(message, i)) for i in range(1,10)]) 
    plt.show()
    
    l_cle = 3
    print(auto_vigenere(message, l_cle))
    