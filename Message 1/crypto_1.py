# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:22:57 2020

@author: tinou_99
"""


#La clé est 1447



with open('message1.txt', 'r') as file:
    message = file.read() 
    

def decrypt(texte, nb):
    # tab = [list(texte[k: k + nb]) for k in range(0,len(texte),nb)]
    return "".join([texte[k::nb] for k in range(0,nb)])


if __name__ == "__main__":
    """
    for e in reversed(sorted(frequences(message).items(), key=lambda t: t[1])):
        print(e)
    """
    """
    for cle in range(1,len(message)):
        print("".join([l[0] for l in decrypt(message, cle) if len(l) != 0]))
        #print("".join(l[0] for l in oui))
    """

    d = {cle: decrypt(message, cle).split("\n")[0] for cle in range(1,1460)}
    
    for k,v in d.items():
        print(k,v)

    #print(decrypt(message, 1447))
        
