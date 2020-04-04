# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:58:22 2020

@author: tinou
"""

import string 


#fréquence avec un dictionnaire
def frequence(texte):
    """
    Prend en argument une chaîne de caractères et renvoie un dictionnaire 
    dont les clés sont les caractères présents dans le texte et les valeurs 
    sont le nombre d'occurences du caractère concerné.
        
    Entrée:
        (str) 
    Sortie:
        (dict()) 
    Test:
        >>> frequence('bonjour') == {'b': 1, 'j': 1, 'n': 1, 'o': 2, 'r': 1, 'u': 1}
        True
    """
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d



#le caractère le plus fréquent
def caractere_plus_frequent(texte):
    """
    Prend en argument une chaîne de caractères et renvoie une liste 
    représentant le classement de manière décroissante de la fréquence
    d'apparition des lettres composants la chaine de caractère saisie.
        
    Entrée:
        (str) 
    Sortie:
        (list) 
    Test:
        >>> mot = "anticonstitutionnellement"
        >>> caractere_plus_frequent(mot) == ['n', 't', 'i', 'e', 'o', 'l', 'c', 'u', 'a', 'm', 's']
        True
    """
    t = list(texte)
    lettres = set(t)
    nb_lettres = sorted(lettres, key = lambda self, other = t: other.count(self), reverse = True)    
    return nb_lettres
    
 
    
#liste des caractères les plus fréquents
def frequence_abc(mot) :
    """
    Prend en argument une chaîne de caractères et renvoie un tuple composé 
    du nombre d'occurance max et une liste des lettres ayant l'occurance 
    la plus élevée (seulement pour des chaînes de caractères comprenant 
    les 26 lettres de l'alphabet français).
        
    Entrée:
        (str) 
    Sortie:
        (tuple) => (int, list)
    Test:
        >>> mot = "anticonstitutionnellement"
        >>> frequence_abc(mot) == (5, ['n', 't'])
        True
    """
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for lettre in mot :
        if lettre in string.ascii_lowercase :
            freq[ord(lettre) - ord('a')] += 1
                 
    sup = [i for i, j in enumerate(freq) if j == (max(freq))] 
    n_freq = []
    for k in sup :
        n_freq.append(string.ascii_lowercase[k]) 
    return max(freq), n_freq




if __name__ == "__main__":
    #print(caractere_plus_frequent("anticonstitutionnellement"))
    print(frequence_abc("anticonstitutionnellement"))
    