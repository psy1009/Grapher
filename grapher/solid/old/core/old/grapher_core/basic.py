import numpy as np
from .errors import *
from .basic_func_classes import *

class Node:
    def __init__(self, func_instance: str, connects: int):
        if type(func_instance) == str:
            if func_instance == '+':
                self.func_instance = Add(connects)
            elif func_instance == '*':
                self.func_instance = Multiply(connects)
            elif func_instance == 'input':
                self.func_instance = Input()
            elif func_instance == 'square':
                self.func_instance = Square(connects)
            
        self.connects = connects
        self.backward_connected_nodes = []
        self.forward_connected_nodes = []
        self.grad = None
        self.forward_args = []
        
    def connect_to(self, node):
        node.backward_connected_nodes.append(self)
        self.forward_connected_nodes.append(node)
        if node.connects < len(node.backward_connected_nodes):
            raise ConnectLimitError(node)
        elif self.connects < len(self.forward_connected_nodes):
            raise ConnectLimitError(self)
    
    def forward(self):
        if len(self.forward_args) == self.connects:
            new_value = self.func_instance.forward(self.forward_args)
            for next_node in self.forward_connected_nodes:
                next_node.forward_args.append(new_value)
                next_node.forward()
            print(type(self.func_instance), 'New value: ', new_value)
            return new_value
    
    def backward(self, inheriting_value: float=1.0):
        print(inheriting_value, self)
        self.grad = inheriting_value
        leaving_values = self.func_instance.backward(inheriting_value)
        if not self.backward_connected_nodes == []:
            for node_idx in range(self.connects):
                self.backward_connected_nodes[node_idx].backward(leaving_values[node_idx])
    