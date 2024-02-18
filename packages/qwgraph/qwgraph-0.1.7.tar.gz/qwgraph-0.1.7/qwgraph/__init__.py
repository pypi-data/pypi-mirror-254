##############################################
##                  Imports                 ##
##############################################
# Maths
import numpy as np
import math 
from math import pi 
# Graph
import networkx as nx 
# Utilities
import copy
from tqdm import tqdm
import pandas as pd
import warnings

from qwgraph import qwgraph as qwfast


##############################################
##             Useful functions             ##
##############################################

def starify(G):
    """
    Starify a graph G and return the dictionnary {node : searchable_edge}.
    """
    nodes = copy.deepcopy(G.nodes())
    s = {}
    for i in nodes:
        G.add_edge(i,f"new_node{i}")
        s[i] = (i,f"new_node{i}")
    return s


###############################################
##                  QW Class                 ##
###############################################

class QW:
    def __init__(self, graph):
        """
        Take a networkx Graph graph, and contruct the associated QW. 
        The coloring is always done the same way using nx.greedy_color with largest_first strategy.
        """
        self.G = copy.deepcopy(graph)
        try:
            self.color = {i:j for i,j in G.nodes.data("color")}
            for i in self.color:
                if self.color[i]== None:
                    raise(Exception)
        except Exception:
            if nx.bipartite.is_bipartite(self.G):
                self.color = nx.bipartite.color(self.G) # Coloring
            else:
                self.color = nx.greedy_color(self.G, strategy="largest_first", interchange=True) # Coloring
            nx.set_node_attributes(self.G, self.color, "color")
            nx.set_node_attributes(graph, self.color, "color")
        self.edges = list(self.G.edges()) # List of edges
        self.index = {self.edges[i]:i for i in range(len(self.edges))} # Index for edges
        self.E = len(self.edges) # Number of edges
        self.N = len(self.color) # Number of nodes

        wiring = [] # For any amplitude self.state[i], says to which node it is connected. Important for the scattering.
        tmp = {list(self.G.nodes)[i]:i  for i in range(self.N)}
        for (i,j) in self.edges:
            if self.color[i]<self.color[j]:
                wiring.append(tmp[i])
                wiring.append(tmp[j])
            else:
                wiring.append(tmp[j])
                wiring.append(tmp[i])

        self.qwf = qwfast.QWFast(wiring,self.N,self.E)
        self.reset()

    def get_proba(self, search):
        """
        Returns the probability to be at one of the searched elements in search.
        """
        return self.qwf.get_proba(search)

    def get_state(self, edges = None):
        """
        Returns a dictionnary {edge : value of the coin}.
        """
        dic = {}
        if type(edges) == type(None):
            edges = list(range(self.E))
        for i in edges:
            dic[self.edges[i]] = np.array([self.qwf.state[2*i],self.qwf.state[2*i+1]],dtype=complex)
        return dic

    def set_state(self, dic):
        """
        Take in parameter a dictionnary {edge : value of the coin}, and change the inner state accordingly.
        """
        for i in range(self.E):
            self.qwf.state[2*i] = dic[self.edges[i]][0]
            self.qwf.state[2*i+1] = dic[self.edges[i]][1]

    def run(self, C, R, ticks=1, search=[]):
        """
        Run the simulation with coin C, oracle R for ticks steps and with searched elements search.
        search contains the index of the marked edges. If you want to search an edge of label e, you can access the coresponding index by using self.index[e].
        """
        self.qwf.run(C,R,ticks,search)
        self.steps+=ticks

    def run_and_get(self, C, R, ticks=1, search = [], progress=True):
        """
        Run the simulation and save the probability of success at each steps.
        If progress is set to True, a progressbar will be dislayed.
        """
        p = {}
        p["step"] = [self.steps]
        p["p_succ"] = [self.get_proba(search)]
        for i in search:
            p[i] = [self.get_proba([i])]
        
        for i in (tqdm(range(ticks))) if progress else (range(ticks)):
            self.run(C,R,ticks=1,search=search)
            
            p["p_succ"].append(self.get_proba(search))
            p["step"].append(self.steps)
            for i in search:
                p[i].append(self.get_proba([i]))
        return pd.DataFrame(p)

    def get_unitary(self, C, R, search = []):
        """
        For a given coin, oracle and set of searched edges, compute and return the unitary U.
        """
        old_state = copy.deepcopy(self.qwf.state)
        U = []
        for i in range(2*self.E):
            self.qwf.state = np.array([int(i==j) for j in range(2*self.E)],dtype=complex)
            self.run(C, R, ticks=1, search=search)
            U.append(copy.deepcopy(self.qwf.state))
        U = np.array(U,dtype=complex).transpose()
        return U

    def reset(self):
        """
        Reset the state to a diagonal one and reset the number of steps.
        """
        self.steps=0
        self.qwf.reset()

    def carac(self, C, R, search=[], waiting=10):
        """
        Give the hitting time and probability of success for a given QW. 
        The waiting parameter is used to accumalate informations about the signal (reccomended to be at least 10).
        """
        self.reset()
        return self.qwf.carac(C,R,search,waiting)

    def carac_multiple(self, C, R, args, waiting=10, nb_proc=1, pbar=True):
        return self.qwf.carac_multiple(C, R, args, waiting, nb_proc, pbar)
