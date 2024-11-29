import listcolouring as lc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import vizing as vz

G = nx.petersen_graph()

n_colours = 6

G = lc.list_init_node(G, range(n_colours - 1), 3, 0)
G = lc.list_init(G, range(n_colours - 1), 3, 0)

G = vz.total_list_colouring_solution(G)

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)

edge_labels = dict([((n1, n2), str(d['colour']) + ': ' + str(d['permissible'])) for n1, n2, d in G.edges(data = True)])
node_labels = dict([(n, str(d['colour']) + ': ' + str(d['permissible'])) for n, d in G.nodes(data = True)])

nx.draw(G,
          pos = G_layout,
   edge_color = list(nx.get_edge_attributes(G, 'colour').values()),
   node_color = list(nx.get_node_attributes(G, 'colour').values()),
        width = 10,
    node_size = 1300,
         cmap = plt.cm.tab10,
    edge_cmap = plt.cm.tab10,
  with_labels = False
)

edge_labels_ = nx.draw_networkx_edge_labels(G, pos = G_layout, edge_labels = edge_labels, font_size = 6)
node_labels_ = nx.draw_networkx_labels(G, pos = G_layout, labels = node_labels, font_size = 6)

patches = [mpatches.Patch(color = plt.cm.tab10(i), label = f'{i}') for i in range(n_colours - 1)]
plt.legend(handles = patches, bbox_to_anchor = (1, 1))

plt.savefig("png/petersen-total.png", format = "PNG")
