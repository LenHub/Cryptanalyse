import matplotlib.pyplot as plt
import numpy as np
from Analyse_frequentielle import Analyse

class CesarX:
"""Cette classe permet de chiffrer, déchiffrer et de trouver la clé d'un texte chiffré
par la méthode de César"""

    def __init__(self,texte):
        self.texte = texte.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def code(self,i):
    """Renvoie le message """
        alphabet = self.alphabet[i:] + self.alphabet[:i]
        code = ''
        for i in self.texte:
            if i in alphabet:
                code += alphabet[self.alphabet.index(i)]
            else:
                code += i
        return code

    def decode(self,i):
    """Renvoie le message en clair d'un texte chiffré par i rotations de l'alphabet"""
        return self.code(-i)

    def _code(self,i):
        self.texte = self.code(i)

    def _decode(self,i):
        self.texte = self.decode(i)

    def cle(self):
      """Analyse pour chaque rotation la corrélation des fréquences
      du texte avec celle de la langue française et renvoie deux 
      graphiques associés """
        X = np.arange(25)

        corr = []

        for i in X:
            texte = self.decode(i)
            ana = Analyse(texte)
            corr.append(ana.correlation())

        m = max(corr)
        im = corr.index(m)
        ana = Analyse(self.decode(im))
        ana.plotfreq()
        plt.plot(X, corr, lw=1)
        plt.xlabel('Décalage')
        plt.ylabel('Correlation')
        plt.title('Correlation en fonction du décalage')
        plt.grid()
        plt.show()
        print('> Décalage :',im)
        print(self.decode(im))

    def _cle(self):
     """Renvoie la clé utilisée pour le chiffrement""" 
        X = np.arange(25)
        corr = []
        for i in X:
            texte = self.decode(i)
            ana = Analyse(texte)
            corr.append(ana.correlation())
        m = max(corr)
        im = corr.index(m)
        return im
