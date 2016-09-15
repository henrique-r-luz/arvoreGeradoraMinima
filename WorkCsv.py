import csv


class WorkCSV:
    fileCSV = ''

    # Imprime a docString associada
    def printDocString(self):
        print(__doc__)

    # Le o arquivo especificado
    def openCSV(self, nameFile, delimitador):
        self.fileCSV = csv.reader(open(nameFile), delimiter=delimitador)

    # Escrevee no arquivo especificado
    def writeCSV(self, nameFile, row):
        self.fileCSV = csv.writer(open(nameFile, "a"))
        self.fileCSV.writerow(row)

    # Percorre o Arquivo
    def listCSV(self):
        lista = []
        for [id, x, y] in self.fileCSV:
                lista.append((id,x,y))
        #lista.remove(('id','x','y'))
        del lista[0]
        return lista
            #print ('Primeiro Nome = %s - Nome do Meio = %s - Ultimo Nome = %s' % (fNome, mNome, lNome))