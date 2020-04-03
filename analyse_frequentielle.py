# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:58:22 2020

@author: tinou
"""
import string 

#fréquence avec un dictionnaire
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



#le caractère le plus fréquent
def caractere_plus_frequent(texte):
    t = list(texte)
    #new_list = []
    lettres = set(t)
    nb_lettres = sorted(lettres, key = lambda self, other = t: other.count(self), reverse = True)    
    return nb_lettres
    
 
    
#liste des caractères les plus fréquents
def frequency(word) :
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for letter in word :
        if letter in string.ascii_lowercase :
            freq[ord(letter) - ord('a')] += 1
                 
    sup = [i for i, j in enumerate(freq) if j == (max(freq))] 
    new_freq = []
    for k in sup :
        new_freq.append(string.ascii_lowercase[k]) 
    return max(freq), new_freq




if __name__ == "__main__":
    #print(caractere_plus_frequent("anticonstitutionnellement"))
    print(frequency("anticonstitutionnellement"))
    