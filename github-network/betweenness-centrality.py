import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
filename = "graphFile.json"
data = {}
with open(filename) as f:
    data = json.load(f)
sizes = {}
labels = {}
# print(data["nodes"][0])
for node in data["nodes"]:
    G.add_node(node["group"], login=node["login"],
               connections=node["connections"], weight=node["weight"])
    sizes[node["group"]] = node["weight"]
    labels[node["group"]] = node["login"]
for link in data["links"]:
    if link["target"] == "no-target":
        continue
    G.add_edge(link["source"], link["target"], weight=1)

largest_component = max(nx.connected_components(G), key=len)
G2 = G.subgraph(largest_component)
pos = nx.fruchterman_reingold_layout(G2)


bc = nx.betweenness_centrality(G2)
labels2 = {i: labels[i] for i in G2.nodes()}
vals = []
for i in G2.nodes():
    vals.append(bc[i] * 10000)
    print(labels2[i], bc[i])

max_bc = -1
label = ""
for profile in bc.keys():
    if bc[profile] > max_bc:
        max_bc = bc[profile]
        label = labels2[profile]
print("Maximum Betweenness Centrality =" + str(max_bc) + ", of user:", label)
nx.draw_networkx(G2, pos, nodelist=G2.nodes(), node_size=vals, labels=labels2,
                 font_family='Product Sans', alpha=0.8, cmap=True)
plt.show()
