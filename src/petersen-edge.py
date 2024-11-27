import listcolouring as lc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import vizing as vz

G = nx.petersen_graph()

G = lc.list_init(G, range(0, 10), 3, 0)

G = vz.edge_list_colouring_solution(G)

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)
edge_colours = nx.get_edge_attributes(G,'colour').values()

nx.draw(G,
        pos = G_layout,
        edge_color = edge_colours,
        with_labels = False,
        edge_cmap = plt.cm.tab10,
        width = 5,
        node_size = 150,
        node_color = 'black')

edge_labels = dict([((n1, n2), str(sorted(d['permissible']))) for n1, n2, d in G.edges(data = True)])
X = nx.draw_networkx_edge_labels(G, pos = G_layout, edge_labels = edge_labels, font_size = 6)

patches = [mpatches.Patch(color = plt.cm.tab10(i), label = f'{i}') for i in range(10)]
plt.legend(handles = patches, bbox_to_anchor = (1.1, 1))

plt.savefig("png/petersen-edge.png", format = "PNG")
