import networkx as nx
from math import sqrt

class Grafo:
    grafo = nx.Graph()
    noGrafo = {1:(4.0,53.0)}
    pos = {}

    def criaGrafo(self,lista):
        for [id, x, y] in lista:
            self.grafo.add_node(int(id),color='blue', pos=(float(x), float(y)))
        self.pos = nx.get_node_attributes(self.grafo, 'pos')
        pos = self.pos.copy()
        self.geraArvoreGeradoraMinima()
        nx.draw(self.grafo, pos, with_labels=False, node_size=20)


    def geraArvoreGeradoraMinima(self):
         if(len(self.pos)!=0):
            distAB= 100000000
            verticeU  = -1
            verticeV = -1
            for no in self.pos:
                for noNewGrafo in self.noGrafo:
                    if(noNewGrafo!=no):
                        distAux = sqrt(((self.pos[no][0] - self.noGrafo[noNewGrafo][0]) ** 2) + ((self.pos[no][1] - self.noGrafo[noNewGrafo][1]) ** 2))
                        if(distAux<distAB):
                            distAB = distAux
                            verticeU = no
                            verticeV = noNewGrafo
            self.noGrafo[verticeU] = self.pos[verticeU]
            self.grafo.add_edge(verticeU,verticeV,weight=distAB)
            del self.pos[verticeU]
            self.geraArvoreGeradoraMinima()
         else:
             return


