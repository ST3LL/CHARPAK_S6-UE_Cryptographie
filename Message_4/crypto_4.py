# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:46 2020

@author: tinou
"""


with open('message4.txt', 'r') as file:
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



def separateur(message):
    pair = []
    impair = []
    for i in range(len(message)):
        if i % 2 == 0:
            pair.append(message[i])
        else:
            impair.append(message[i])
    return pair, impair



def colleur(pair, impair):
    n_msg = []
    for i in range(len(pair)):
        n_msg.append(pair[i])
        n_msg.append(impair[i])
    return ''.join(n_msg)



def cle_probable(message):
    carac = frequences(message)
    carac_max = max([(carac[e], e) for e in carac], key= lambda x : x[0])
    cle = ord(carac_max[1]) - ord(' ') 
    return cle



def cesar_dechiffrage(lettre, cle):
    return (ord(lettre) - cle)


#c'est très très moche
def cesar(message):
    n_msg_p = []
    n_msg_i = []
    m = separateur(message)
    pair = m[0]
    impair = m[1]
    p_cle = cle_probable("".join(pair))
    i_cle = cle_probable("".join(impair))
    for l in pair:
        p_crypt = chr(cesar_dechiffrage(l, p_cle))
        n_msg_p.append(p_crypt)
    for e in impair :
        i_crypt = chr(cesar_dechiffrage(l, i_cle))
        n_msg_i.append(i_crypt)
    new = colleur(n_msg_p, n_msg_i)
    return new



if __name__ == "__main__":
    print(cesar(message))
    

    
    