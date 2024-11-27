import listcolouring as lc
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import vizing as vz

G = nx.petersen_graph()
G = lc.list_init_node(G, range(0, 10), 3, 0)
G = vz.node_list_colouring_solution(G)

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)

node_labels = dict([(n, str(sorted(d['permissible']))) for n, d in G.nodes(data = True)])

node_colors = set(nx.get_node_attributes(G, 'colour').values())

nx.draw(G,
        G_layout,
         edge_color = "black",
         node_color = list(nx.get_node_attributes(G, 'colour').values()),
              width = 4,
          node_size = 1000,
               cmap = plt.cm.tab10,
             labels = node_labels,
          font_size = 6,
        with_labels = True
)

patches = [mpatches.Patch(color = plt.cm.tab10(i), label = f'{i}') for i in range(1, 10)]
plt.legend(handles = patches, bbox_to_anchor = (1, 1))

plt.savefig("png/petersen-node.png", format = "PNG")
