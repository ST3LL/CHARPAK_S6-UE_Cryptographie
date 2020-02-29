# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:46 2020

@author: tinou
"""

#La clé est 8


with open('message3.txt', 'r') as file:
    message = file.read() 
#print(message)


def cesar_chiffrage(nb, decalage):
    return(nb + decalage)
    
def cesar_dechiffrage(nb, decalage):
    return(nb - decalage)
    

def cesar(message, decalage):
    new_message = []
    for l in message:
        unicode = ord(l) 
        crypt = cesar_chiffrage(unicode, decalage)
        new_message.append(chr(crypt))
    new_message = "".join(new_message)
    return(new_message)
    

if __name__ == "__main__":  
    for i in range(25, 50):
        print("Clé : ", i)
        print(cesar(message, i))
        print("_____________________________________________")

   


