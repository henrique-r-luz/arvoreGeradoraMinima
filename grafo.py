import networkx as nx
from math import sqrt

class Grafo:
    grafo = nx.Graph()
    noGrafo = {1:(4.0,53.0)}
    pos = {}
    profundidade  = 2
    valorArestaReferencia = []

    def criaGrafo(self,lista):
        for [id, x, y] in lista:
            self.grafo.add_node(int(id),color='blue', pos=(float(x), float(y)))
        self.pos = nx.get_node_attributes(self.grafo, 'pos')
        pos = self.pos.copy()
        self.geraArvoreGeradoraMinima()
        nx.draw(self.grafo, pos, with_labels=True, node_size=200)
        self.validaAresta((9,14))


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


    def validaAresta(self,aresta):
        a,b = aresta
        self.valorArestaReferencia = []
        self.calculaProximidade(a,b,0)
        print(self.valorArestaReferencia)

    def calculaProximidade(self,vertice,verticeNaoAnalisado,contaProfundidade):
        if contaProfundidade < self.profundidade:
            for n in self.grafo.adjacency_iter():
                if n[0]==vertice:
                    contaProfundidade = contaProfundidade+1
                    conjuntoVertice = n[1]
                    del conjuntoVertice[verticeNaoAnalisado]
                    print(conjuntoVertice)
                    for no in conjuntoVertice.keys():
                        self.valorArestaReferencia.append(conjuntoVertice[no]['weight'])
                        self.calculaProximidade(no,vertice,contaProfundidade)





