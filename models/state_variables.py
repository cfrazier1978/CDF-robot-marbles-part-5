import networkx as nx

# define global variables
T = 25 #iterations in our simulation
boxes=5 #number of boxes in our network
m= 2 #for barabasi graph type number of edges is (n-2)*m

# create graph object with the number of boxes as nodes
network = nx.barabasi_albert_graph(boxes, m)

genesis_states = {'network':network}