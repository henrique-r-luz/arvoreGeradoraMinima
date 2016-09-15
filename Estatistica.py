import numpy as np
from math import sqrt


class Estatistica:
    
    def dPAmostral(self, elementos):
        NPelementos = np.array(elementos)
        soma = 0
        if len(elementos) == 1:
            devioAmostral = 1
        else:
            for item in elementos:
                soma += ((item - NPelementos.mean()) ** 2)
            devioAmostral = sqrt(soma / (len(elementos) - 1))
        return devioAmostral




#est = Estatistica()
#print(est.dPAmostral((3.60,2.82,5.38,3.60,4.24)))
