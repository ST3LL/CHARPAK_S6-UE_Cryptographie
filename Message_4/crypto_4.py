# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:46 2020

@author: tinou
"""


with open('message4.txt', 'r') as file:
    message = file.read() 



def frequences(texte):
    d = dict()
    for l in texte:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d



def cle_probable(n_carac):
    carac = frequences(n_carac)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle



def cesar_dechiffrage(lettre, cle):
    return (ord(lettre) - cle)
    
    

def cesar(message, cle):
    new_message = []
    m = list(message)
    for l in m:
        crypt = chr(cesar_dechiffrage(l, cle))
        new_message.append(crypt)
    new = "".join(new_message)
    return new



def auto_cesar(message):
    pair, impair = separateur(message)
    return colleur((cesar(pair, cle_probable(pair)), cesar(impair, cle_probable(impair))))



def separateur(message):
    pair = []
    impair = []
    for c in range(len(message)):
        if c % 2 == 0:
            pair.append(message[c])
        else:
            impair.append(message[c])
    return pair, impair


"""
def plus_longue_liste(m):
    n_m = 0
    for i in m:
        if len(m[i]) < len(m[i+1]):
            n_m = len(m[i+1])
        else:
            n_m = len(m[i])
    return n_m
    
 """           


def colleur(v_msg):
    n_msg = []
    for c in range(len(v_msg[0])):
        for e in range(len(v_msg[0])):
            try : 
                n_msg.append(v_msg[e][c])
            except : 
                pass
    return ''.join(n_msg)



"""
def vigenere(text, key):
    text = [i for i in text]
    encrypted = [cesar(text[i], key[i]) for i in range(len(text))]
    return "".join(encrypted)
"""


if __name__ == "__main__" :
    print(auto_cesar(message))
    #print(plus_longue_liste([['a', 'a', 'a'], ['b', 'b'], ["c","c","c","c"]]))
    #print(colleur([['a', 'a', 'a'], ['b', 'b']]))

    
    