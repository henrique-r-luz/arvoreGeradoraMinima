import networkx as nx
from math import sqrt
import numpy as np
from Estatistica import Estatistica

class Grafo:
    grafo = nx.Graph()
    noGrafo = {43:(63,139)}
    pos = {}
    profundidade  = 2
    valorArestaReferencia = []
    arestaRemovidas = []

    def criaGrafo(self,lista):
        for [id, x, y] in lista:
            self.grafo.add_node(int(id), pos=(float(x), float(y)))
        self.pos = nx.get_node_attributes(self.grafo, 'pos')
        pos = self.pos.copy()
        self.geraArvoreGeradoraMinima()
        for u, v, d in self.grafo.edges(data=True):
            self.validaAresta(u,v)
        self.grafo.remove_edges_from(self.arestaRemovidas)
        nx.draw(self.grafo, pos, with_labels=True, node_size=200)
        #nx.draw_networkx_edge_labels(self.grafo, pos)



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





    def validaAresta(self, u,v):

        flagV = False
        flagU = False
        est = Estatistica()
        self.valorArestaReferencia = []
        self.calculaProximidade(u, v, 0)
        valor = np.array(self.valorArestaReferencia)
        calculoAresta = valor.mean() + (est.dPAmostral(self.valorArestaReferencia)*self.profundidade)
        #if  u==64 :
        print(self.grafo[u][v]['weight'])
        if self.grafo[u][v]['weight'] > calculoAresta:
            flagU = True

        self.valorArestaReferencia = []
        self.calculaProximidade(v, u, 0)
        valor = np.array(self.valorArestaReferencia)
        calculoAresta = valor.mean() + (est.dPAmostral(self.valorArestaReferencia)*self.profundidade)
        #if  v==64 :
         #    print(calculoAresta)
        if self.grafo[v][u]['weight'] > calculoAresta:
            flagV = True

        if flagV and flagU:
            self.arestaRemovidas.append((u,v))







    def calculaProximidade(self,vertice,verticeNaoAnalisado,contaProfundidade):
        vizinhos  = self.grafo.neighbors(vertice)
        i = vizinhos.index(verticeNaoAnalisado)
        del vizinhos[i]
        if(len(vizinhos)!=0):
            if contaProfundidade < self.profundidade:
                for no in vizinhos:
                    self.valorArestaReferencia.append(self.grafo[no][vertice]['weight'])
                    novoContador = contaProfundidade+1
                    self.calculaProximidade(no,vertice,novoContador)
        else:
            self.valorArestaReferencia.append(self.grafo[vertice][verticeNaoAnalisado]['weight'])





