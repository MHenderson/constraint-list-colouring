import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import listcolouring
from listcolouring import list_init_node

import vizing
from vizing import list_colouring_solution

G = nx.petersen_graph()
G = list_init_node(G, range(1, 10), 3, 0)
G = list_colouring_solution(G)

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)

node_labels = dict([(n, str(d['colour']) + ': ' + str(d['permissible'])) for n, d in G.nodes(data = True)])

node_colors = set(nx.get_node_attributes(G, 'colour').values())

patches = [mpatches.Patch(color = plt.cm.tab10(i), label = f'{i}') for i in node_colors]

nx.draw(G,
        G_layout,
        edge_color = "black",
        node_color = list(nx.get_node_attributes(G, 'colour').values()),
        node_shape = 's',
        width = 10,
        node_size = 1300,
        cmap = plt.cm.tab10,
        labels = node_labels,
        font_size = 6,
        with_labels = True
)

plt.legend(handles = patches, title = "Colours", bbox_to_anchor = (1, 1))

plt.savefig("png/petersen-node.png", format = "PNG")
