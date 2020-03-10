# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:46 2020

@author: tinou
"""
#La clé est 263


with open('message3.txt', 'r') as file:
    message = file.read() 
#print(message)

def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d


def cesar_chiffrage(nb, decalage):
    return(nb + decalage)
    
def cesar_dechiffrage(nb, decalage):
    return(nb - decalage)
    

def cesar(message, decalage):
    new_message = []
    for l in message:
        unicode = ord(l) 
        crypt = cesar_dechiffrage(unicode, decalage)
        new_message.append(chr(crypt))
    new_message = "".join(new_message)
    
    return(new_message)
        
    

if __name__ == "__main__":
    fs = frequences(message)
    lettre_max = max([(fs[e], e) for e in fs], key= lambda x : x[0])
    #print(lettre_max)
    #print(ord(lettre_max[1]))
    #print(ord(" "))
    
    nb_cod = ord(lettre_max[1])
    nb_freq = ord(" ")
    nb = nb_cod - nb_freq
    print(nb)
    print(cesar(message, nb))
    
    
    
    