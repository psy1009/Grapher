import numpy as np

from grapher.solid import Graph, FuncNode

class Network(Graph):
    def __init__(self, nodes: list[FuncNode]=[]):
        super().__init__()
        self.trainable = True
        self.optimizer = None
        self.nodes = nodes
    