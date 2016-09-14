__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx


def geraPosicao(listaObj):
    pos ={}
    for [id, x, y] in listaObj:
        pos[int(id)] = (int(x),int(y))
    return posz

G=nx.Graph()
# explicitly set positions
pos={0:(1,1),
     1:(1,0),
     2:(0,1),
     3:(1,1),
     4:(0.5,2)}

G=nx.Graph(pos)

nx.draw_networkx_nodes(G,pos,node_size=2000)

#nx.draw_networkx_nodes(G,pos,node_size=2000,nodelist=[4])
#nx.draw_networkx_nodes(G,pos,node_size=3000,nodelist=[0,1,2,3],node_color='b')
#nx.draw_networkx_edges(G,pos,alpha=0.5,width=6)
#nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
plt.axis('on')
plt.savefig("house_with_colors.png") # save as png
plt.show() # display