import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define global variables
T = 25 #iterations in our simulation
boxes=5 #number of boxes in our network
m= 2 #for barabasi graph type number of edges is (n-2)*m

# create graph object with the number of boxes as nodes
network = nx.barabasi_albert_graph(boxes, m)

# add balls to box nodes
for node in network.nodes:
    network.nodes[node]['balls'] = np.random.randint(1,10)

#Behavior: node by edge dimensional operator
#input the states of the boxes output the deltas along the edges

# We specify the robotic networks logic in a Policy/Behavior Function
# unlike previous examples our policy controls a vector valued action, defined over the edges of our network
def robotic_network(params, step, sH, s):
    network = s['network']
    delta_balls = {}
    for e in network.edges:
        src = e[0]
        dst = e[1]
        #transfer one ball across the edge in the direction of more balls to less
        delta_balls[e] = np.sign(network.nodes[src]['balls']-network.nodes[dst]['balls'])
    return({'delta': delta_balls})


    #mechanism: edge by node dimensional operator
#input the deltas along the edges and update the boxes

# We make the state update functions less "intelligent",
# ie. they simply add the number of marbles specified in _input 
# (which, per the policy function definition, may be negative)

def update_network(params, step, sH, s, _input):
    network = s['network'] 
    delta_balls = _input['delta']
    for e in network.edges:
        move_ball = delta_balls[e]
        src = e[0]
        dst = e[1]
        if (network.nodes[src]['balls'] >= move_ball) and (network.nodes[dst]['balls'] >= -move_ball):
            network.nodes[src]['balls'] = network.nodes[src]['balls']-move_ball
            network.nodes[dst]['balls'] = network.nodes[dst]['balls']+move_ball
            
    return ('network', network)

    #NetworkX helper functions
def get_nodes(g):
    return [node for node in g.nodes if g.nodes[node]]


def pad(vec, length,fill=True):

    if fill:
        padded = np.zeros(length,)
    else:
        padded = np.empty(length,)
        padded[:] = np.nan
        
    for i in range(len(vec)):
        padded[i]= vec[i]
        
    return padded

def make2D(key, data, fill=False):
    maxL = data[key].apply(len).max()
    newkey = 'padded_'+key
    data[newkey] = data[key].apply(lambda x: pad(x,maxL,fill))
    reshaped = np.array([a for a in data[newkey].values])
    
    return reshaped

    df['Balls'] = df.network.apply(lambda g: np.array([g.nodes[j]['balls'] for j in get_nodes(g)]))

